"""
Helena Herrera Aviles
1/2/24
exercici 1
"""
try:
    def est_paraules(paraules):
        if not paraules:
            return None, None, None
        paraula_llarga = max(paraules, key=len, default="")
        paraula_curta = min(paraules, key=len, default="")
        mitjana_mida = sum(len(paraula) for paraula in paraules) / len(paraules)
        return paraula_llarga, paraula_curta, mitjana_mida
    def main():
        paraules = []

        while (paraula := input("Introdueix una paraula (o escriu '\\q' per sortir): ")) != "\\q":
            paraules.append(paraula)

        paraula_llarga, paraula_curta, mitjana_mida = est_paraules(paraules)

        print("\nResultats:")
        print(f"Paraula més llarga: {paraula_llarga}")
        print(f"Paraula més curta: {paraula_curta}")
        print(f"Mida mitjana de les paraules: {mitjana_mida:.2f}")

    if __name__ == "__main__":
        main()
except:
    print("així no era")
