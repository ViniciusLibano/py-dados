class ClassesT20:
    def __init__(
        self, 
        id   : int, 
        desc : str, 
        pv   : int, 
        pm   : int, 
        per  : str,
        pro  : str,
        hab  : str
    ):
        self.id   : int = id
        self.desc : str = desc
        self.pv   : int = pv
        self.pm   : int = pm
        self.per  : list[str] = per.split(";") if per else None
        self.pro  : list[str] = pro.split(";") if pro else None
        self.hab  : list[str] = hab.split(";") if hab else None


classes = [
    'Arcanista',
    'Barbaro',
    'Bardo',
    'Bucaneiro',
    'Cacador',
    'Cavaleiro',
    'Clerigo',
    'Druida',
    'Guerreiro',
    'Inventor',
    'Ladino',
    'Lutador',
    'Nobre',
    'Paladino'
]

racas = [
    'Humano',
    'Anao',
    'Dahllan',
    'Elfo',
    'Goblin',
    'Lefou',
    'Minotauro',
    'Qareen',
    'Golem',
    'Hynne',
    'Kliren',
    'Medusa',
    'Osteon',
    'Sereia/Tritao',
    'Silfide',
    'Suraggel',
    'Trog'
]

origens = [
    'Acolito',
    'Amigo dos Animais',
    'Amnesico',
    'Aristocrata',
    'Artesao',
    'Artista',
    'Assistente de Laboratorio',
    'Batedor',
    'Capanga',
    'Charlatao',
    'Circense',
    'Criminoso',
    'Curandeiro',
    'Eremita',
    'Escravo',
    'Estudioso',
    'Fazendeiro',
    'Forasteiro',
    'Gladiador',
    'Guarda',
    'Herdeiro',
    'Heroi Campones',
    'Marujo',
    'Mateiro',
    'Membro de Guilda',
    'Mercador',
    'Minerador',
    'Nomade',
    'Pivete',
    'Refugiado',
    'Seguidor',
    'Selvagem',
    'Soldado',
    'Taverneiro',
    'Trabalhador'
]