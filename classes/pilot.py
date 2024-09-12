class pilot:
    def __init__(self, name,skill_level):
        self.name = name
        self.skill_level = skill_level

    def __repr__(self):
        return f"Pilot(name={self.name}, skill_level={self.skill_level})"

