CREATE TABLE classes (
    id_classe INTEGER PRIMARY KEY ASC,
    ds_classe TEXT(50),
    pv_classe INTEGER,
    pm_classe INTEGER,
    pericias TEXT(255),
    proficiencias TEXT(255),
    habilidades TEXT(255)
);

INSERT INTO classes (
    ds_classe,
    pv_classe,
    pm_classe,
    pericias,
    proficiencias,
    habilidades
)
VALUES (
    'Arcanista',
    8,
    6,
    'Misticismo;Vontade;+1 entre Conhecimento, Iniciativa, Ofício e Percepção',
    NULL,
    'Caminho do Arcanista'
);

INSERT INTO classes (
    ds_classe,
    pv_classe,
    pm_classe,
    pericias,
    proficiencias,
    habilidades
)
VALUES (
    'Bárbaro',
    24,
    3,
    'Fortitude;Luta',
    'Armas marciais;Escudos',
    'Fúria'
);