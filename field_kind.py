# -*- coding: utf-8 -*-
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=False)
class FieldKind:
    """Examines the class FieldKindEnum to find fields. 
    """
    index: int
    field_name: str
    alias_field: str


class FieldKindEnum(Enum):
    """Enum Class consist of selected layer fields and its created aliases as members.
    """
    NUMER_POWIERZCHNI = FieldKind(
        index=0,
        field_name="a_i_num",
        alias_field="NUMER POWIERZCHNI",
    )
    ADRES_LESNY = FieldKind(
        index=1,
        field_name="adr_for",
        alias_field="ADRES LEŚNY",
    )
    RODZAJ_POWIERZCHNI = FieldKind(
        index=2,
        field_name="area_type",
        alias_field="RODZAJ POWIERZCHNI",
    )
    TYP_SIEDLISKOWY_LASU = FieldKind(
        index=3,
        field_name="site_type",
        alias_field="TYP SIEDLISKOWY LASU",
    )
    GOSPODARSTWO = FieldKind(
        index=4,
        field_name="silvicult",
        alias_field="GOSPODARSTWO",
    )
    FUNKCJA_LASU = FieldKind(
        index=5,
        field_name="forest_fun",
        alias_field="FUNKCJA LASU",
    )
    BUDOWA_PIONOWA_DRZEWOSTANU = FieldKind(
        index=6,
        field_name="stand_stru",
        alias_field="BUDOWA PIONOWA DRZEWOSTANU",
    )
    WIEK_REBNOSCI = FieldKind(
        index=7,
        field_name="rotat_age",
        alias_field="WIEK RĘBNOŚCI",
    )
    POWIERZCHNIA_HA = FieldKind(
        index=8,
        field_name="sub_area",
        alias_field="POWIERZCHNIA (ha)",
    )
    KATEGORIE_OCHRONNOSCI = FieldKind(
        index=9,
        field_name="prot_categ",
        alias_field="KATEGORIE OCHRONNOŚCI",
    )
    KOD_GATUNKU_PANUJACEGO = FieldKind(
        index=10,
        field_name="species_cd",
        alias_field="KOD GATUNKU PANUJĄCEGO",
    )
    UDZIAŁ_GATUNKU_PANUJACEGO = FieldKind(
        index=11,
        field_name="part_cd",
        alias_field="UDZIAŁ GATUNKU PANUJĄCEGO",
    )
    WIEK_GATUNKU_PANUJACEGO = FieldKind(
        index=12,
        field_name="spec_age",
        alias_field="WIEK GATUNKU PANUJĄCEGO",
    )
    ROK_STANU_DANYCH = FieldKind(
        index=13,
        field_name="a_year",
        alias_field="ROK STANU DANYCH",
    )
