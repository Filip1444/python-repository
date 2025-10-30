def prosjek(ime, *args):
    prosjek = sum(args) / len(args)
    
    print(f"prosjek učenika {ime} je {prosjek}")
          

ime = "filip"
ocjene = [5, 4, 3, 4, 1, 2, 3, 4, 5]

prosjek(ime, *ocjene)
