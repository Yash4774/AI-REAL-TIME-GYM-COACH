import time
import json
import streamlit as st
import streamlit.components.v1 as components


class VoicePipeline:
    def __init__(self, llm, tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0
        self.next_voice_at = 0

    def _find_form_issue(self, exercise, metrics):
        if "issue" in metrics:
            return metrics["issue"]
        
        if exercise == "Squats":
            depth = metrics.get("depth_status", "")
            back_angle = metrics.get("back_angle", 180)

            if depth == "TOO HIGH":
                return "The user's squat is not deep enough - knees are not bending sufficiently."
            
            if isinstance(back_angle, (int, float)) and back_angle < 130:
                return "The user is learning too far forward during the squat."
            
        elif exercise == "Push-Ups":
            alignment = metrics.get("body_alignment", "")
            hip_status = metrics.get("hip_status", "")

            if alignment == "Poor Form":
                return "The user's body is not straight during the push-up."
            
            if hip_status == "SAGGING":
                return "The user's hips are sagging down during the push-up."
            
            if hip_status == "PICKED UP":
                return "The user's hips are too high - lower them to form a straight line."
            
        elif exercise == "Biceps Curls (Dumbbell)":
            swing = metrics.get("swing_status", "")
            shoulder = metrics.get("shoulder_status", "")

            if swing == "SWINGING":
                return "The user is swinging their torso during the curl - keep the body still."
            
            if shoulder == "ELBOW DRIFTING":
                return "The user's elbow is drifting away from their side during curl."
            
        elif exercise == "Shoulder Press":
            back_arch = metrics.get("back_arch_status", "")
            extension = metrics.get("extension_status", "")

            if back_arch == "Excessive Arch":
                return "The user is arching their lower back excessively during the press."
            
            if back_arch == "Slight Arch":
                return "Slight back arch detected - encourage the user to brace their core."
            
        elif exercise == "Lunges":
            balance = metrics.get("balance_status", "")

            if balance == "OFF BALANCE":
                return "The user is losing balance during the lunge - feet should be hip-width apart."
            
        return None
    



    def process_event(self, event, exercise, metrics):
        issue = self._find_form_issue(exercise, metrics)

        now = time.time()

        is_major_issue = event in ["workout_started", "set_completed", "workout_completed", "no_pose_detected", "rep_completed"]
        can_interrupt = event in ["workout_started", "workout_completed"]

        if now < self.next_voice_at and not can_interrupt:
            return None

        if not is_major_issue:
            if now - self.last_spoken_at < 12:
                return None
            
            if not issue:
                event = "motivation"
            
        text = self.llm.give_feedback(event, issue)

        try:
            voice = self.tts.speak(text)
        except Exception as e:
            voice = None
            st.session_state.voice_pipeline_error = f"Audio generation failed: {e}"

        self.last_spoken_at = now
        self.next_voice_at = now + self._estimate_speech_seconds(text)

        st.session_state.voice_pause_until = self.next_voice_at


        return voice, text

    def _estimate_speech_seconds(self, text):
        words = len((text or "").split())
        return max(8, min(22, 3 + words * 0.65))
    

def autoplay_audio(audio_bytes=None, text=None):
    if not text and not audio_bytes:
        return

    if text:
        text_json = json.dumps(text)
        components.html(
            f"""
            <script>
            (function() {{
                const text = {text_json};
                if (!text || !("speechSynthesis" in window)) return;
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = "en-US";
                utterance.rate = 0.92;
                utterance.pitch = 1.0;
                window.speechSynthesis.speak(utterance);
            }})();
            </script>
            """,
            height=0,
        )
        return

    import base64
    audio_base64 = base64.b64encode(audio_bytes).decode()
    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )
    
        
    


