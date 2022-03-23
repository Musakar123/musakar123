class Hewan:
    def __init__(self, inputNama, inputJenis_mkn, inputHabitat):
        self.nama = inputNama
        self.jenis_mkn = inputJenis_mkn
        self.habitat = inputHabitat

animal_1 = Hewan("buaya","Karnivora","air")
animal_2 = Hewan("kuda","Herbivora","Darat")
animal_3 = Hewan("elang","Karnivora","Darat")

print(animal_1.nama,animal_1.jenis_mkn,animal_1.habitat)
print(animal_2.nama,animal_2.jenis_mkn,animal_2.habitat)
print(animal_3.nama,animal_3.jenis_mkn,animal_3.habitat)

