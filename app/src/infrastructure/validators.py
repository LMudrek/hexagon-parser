def validate_arn(arn: str) -> None:

    if not arn.startswith("arn:aws:"):

        raise ValueError("Invalid AWS ARN")
