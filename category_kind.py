# -*- coding: utf-8 -*-
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryKind:
    """Examines the class CategoryKindEnum to find fields. 
    """
    category: str
    code: str


class CategoryKindEnum(Enum):
    """Enum Class consist of kind of protection categories as members.
    """

    WSZYSTKIE_KATEGORIE_OCHRONNOSCI = CategoryKind(
        category="wszystkie kategorie ochronności",
        code="OCH")

    GLEBOCHRONNE = CategoryKind(
        category="glebochronne",
        code="OCH GLEB")

    WODOCHRONNE = CategoryKind(
        category="wodochronne",
        code="OCH WOD")

    TRWALE_USZKODZONE_PRZEMYSLOWO = CategoryKind(
        category="trwale uszkodzone przemysłowo",
        code="OCH USZK")

    STALE_POWIERZCHNIE_DOSWIADCZALNE = CategoryKind(
        category="stałe powierzchnie doświadczalne",
        code="OCH BADAW")

    NASIENNE = CategoryKind(
        category="nasienne",
        code="OCH NAS")

    OSTOJE_ZWIERZAT = CategoryKind(
        category="ostoje zwierząt",
        code="OCH OSTOJ")

    W_MIASTACH_I_WOKOL_MIAST = CategoryKind(
        category="w miastach i wokół miast",
        code="OCH MIAST")

    UZDROWISKOWE = CategoryKind(
        category="uzdrowiskowe",
        code="OCH UZDR")

    OBRONNE = CategoryKind(
        category="obronne",
        code="OCH OBR")
