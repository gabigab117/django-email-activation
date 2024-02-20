from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return f"{user.is_active}{user.pk}{timestamp}"


email_verification_token = EmailVerificationTokenGenerator()
