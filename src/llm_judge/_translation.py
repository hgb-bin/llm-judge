#!/usr/bin/env python3

# 2026 (c) Micha Birklbauer
# https://github.com/michabirklbauer/

# ruff: noqa: N818

from pydantic import BaseModel, Field

from typing import Literal


class TranslationError(BaseModel):
    error_type: Literal[
        "accuracy",
        "fluency",
        "style",
        "terminology",
        "non-translation",
        "other",
        "no-error",
    ] = Field(
        description=(
            "The type of translation error: "
            "One of 'accuracy', 'fluency', 'style', 'terminology', 'non-translation', 'other', or 'no-error'."
        )
    )
    error_subtype: Literal[
        "addition",
        "mistranslation",
        "omission",
        "untranslated text",
        "character encoding",
        "grammar",
        "inconsistency",
        "punctuation",
        "register",
        "spelling",
        "awkward",
        "inappropriate for context",
        "inconsistent use",
        "no-subtype",
    ] = Field(
        description=(
            "The error subtype which can be for 'accuracy': 'addition', 'mistranslation', 'omission', 'untranslated text'; "
            "for 'fluency': 'character encoding', 'grammar', 'inconsistency', 'punctuation', 'register', 'spelling'; "
            "for 'style': 'awkward'; for 'terminology': 'inappropriate for context', 'inconsistent use'."
        )
    )
    error_severity: Literal["critical", "major", "minor"] = Field(
        description="Error severity which is one of 'critical', 'major', and 'minor'."
    )
    error_index_start: int = Field(
        ge=0,
        description="The start index in the machine translation where the error occurs (inclusive) using 0-based indexing.",
    )
    error_index_end: int = Field(
        ge=0,
        description="The end index in the machine translation where the error occurs (inclusive) using 0-based indexing.",
    )
    description: str = Field(
        description="A detailed description of the translation error and how to improve the translation."
    )
    location: str = Field(
        description="Where in the machine translation the error is located given as a substring."
    )


class TranslationErrorAccuracy(TranslationError):
    error_type: Literal["accuracy",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'accuracy' for this type of translation error."
        )
    )
    error_subtype: Literal[
        "addition",
        "mistranslation",
        "omission",
        "untranslated text",
    ] = Field(
        description=(
            "The error subtype which can be for 'accuracy': 'addition', 'mistranslation', 'omission', 'untranslated text'."
        )
    )


class TranslationErrorFluency(TranslationError):
    error_type: Literal["fluency",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'fluency' for this type of translation error."
        )
    )
    error_subtype: Literal[
        "character encoding",
        "grammar",
        "inconsistency",
        "punctuation",
        "register",
        "spelling",
    ] = Field(
        description=(
            "The error subtype which can be for 'fluency': 'character encoding', 'grammar', 'inconsistency', 'punctuation', 'register', 'spelling'."
        )
    )


class TranslationErrorStyle(TranslationError):
    error_type: Literal["style",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'style' for this type of translation error."
        )
    )
    error_subtype: Literal["awkward",] = Field(
        description=("The error subtype which can be for 'style': 'awkward'.")
    )


class TranslationErrorTerminology(TranslationError):
    error_type: Literal["terminology",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'terminology' for this type of translation error."
        )
    )
    error_subtype: Literal[
        "inappropriate for context",
        "inconsistent use",
    ] = Field(
        description=(
            "The error subtype which can be for 'terminology': 'inappropriate for context', 'inconsistent use'."
        )
    )


class TranslationErrorNontranslation(TranslationError):
    error_type: Literal["non-translation",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'non-translation' for this type of translation error."
        )
    )
    error_subtype: Literal["no-subtype",] = Field(
        description=(
            "The error subtype which can be for 'non-translation': 'no-subtype'."
        )
    )


class TranslationErrorOther(TranslationError):
    error_type: Literal["other",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'other' for this type of translation error."
        )
    )
    error_subtype: Literal["no-subtype",] = Field(
        description=("The error subtype which can be for 'other': 'no-subtype'.")
    )


class TranslationErrorNoerror(TranslationError):
    error_type: Literal["no-error",] = Field(
        description=(
            "The type of translation error: "
            "Should be 'no-error' for this type of translation error - which means this "
            "translation is error free. It is better to not report an error instead of "
            "using 'no-error'!"
        )
    )
    error_subtype: Literal["no-subtype",] = Field(
        description=("The error subtype which can be for 'no-error': 'no-subtype'.")
    )


class QualityEstimation(BaseModel):
    quality_estimation_value: float = Field(
        ge=0.0,
        le=1.0,
        description=(
            "The quality estimation of the translation given as a value between 0 and 1 "
            "where 0 is complete gibberish and 1 would be a perfect translation."
        ),
    )


class QualityEstimationAnnotated(QualityEstimation):
    source: str = Field(description="The source text.")
    machine_translation: str = Field(description="The machine translation text.")
    errors: list[
        TranslationErrorAccuracy
        | TranslationErrorFluency
        | TranslationErrorStyle
        | TranslationErrorTerminology
        | TranslationErrorNontranslation
        | TranslationErrorOther
        | TranslationErrorNoerror
    ] = Field(min_length=0, description="List of all translation errors.")
