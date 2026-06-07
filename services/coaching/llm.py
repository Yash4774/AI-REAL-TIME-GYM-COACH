from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]

        if not self.client:
            return self._fallback_feedback(event, issue)

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.4
            )
            text = response.choices[0].message.content.strip()
        except Exception:
            text = self._fallback_feedback(event, issue)

        self.history.append({"role": "user", "content": prompt})
        self.history.append({"role": "assistant", "content": text})

        return text

    def _fallback_feedback(self, event, issue):
        if issue:
            return issue.replace("The user is", "You are").replace("The user's", "Your")

        if event == "workout_started":
            return "Workout started. Stay strong, control each rep, and keep your form sharp."

        if event == "set_completed":
            return "Set complete. Great work, breathe steady, and get ready for the next round."

        if event == "workout_completed":
            return "Workout complete. Excellent effort today, recover well and stay consistent."

        if event == "no_pose_detected":
            return "Step into the camera frame so I can track your form clearly."

        return "Keep going. Stay controlled, brace your core, and maintain clean form."





