class Animal:

    def __init__(self, birth_type="Unknown",
                 appearance="Unknown", bloodType="Unknown"):
        self.birth_type = birth_type
        self.appearance = appearance
        self.bloodType = bloodType

    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    @property
    def appearance(self):
        return self.__appearance
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def bloodType(self):
        return self.__bloodType

    @bloodType.setter
    def bloodType(self, bloodType):
        self.__bloodType = bloodType

    def __str__(self):
        return ("A {} is {} it is {} it is {}"
                .format(type(self).__name__, self.birth_type,
                        self.appearance, self.bloodType))

    class Mamal(Animal):
        def __init__(self, birthType="born alive",
                     appearance="hair or fur",
                     bloodType="warm blooded",
                     nurseYoung="True"):
            Animal.__init__(self, birthType, appearance)
            self.__nurseYoung = nurseYoung

        @property
        def nurseYoung(self):
            return self.__nurseYoung

        @nurseYoung.setter
        def nurseYoung(self, nurseYoung):
            self.__nurseYoung = nurseYoung

        def __str__(self):
            return super().__str__() + " and it is {} they nurse" \
        " their young".format(self.nurseYoung)
