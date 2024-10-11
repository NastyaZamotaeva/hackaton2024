high_energy_physics_keywords = {
    "neutrino oscillations",
    "flavor physics",
    "deep inelastic scattering",
    "higgs boson",
    "beam energy",
    "hadronization",
    "cyclotron",
    "quark-gluon plasma",
    "beam dynamics",
    "higgs field",
    "energy frontier",
    "string theory",
    "perturbative qcd",
    "renormalization",
    "weak force",
    "quantum tunneling",
    "electromagnetic radiation",
    "magnetic monopoles",
    "gauge bosons",
    "atmospheric neutrinos",
    "bosons",
    "quantum chromodynamics",
    "majorana particles",
    "polarization",
    "neutrino telescopes",
    "calorimetry",
    "lattice gauge theory",
    "dark energy",
    "holographic principle",
    "primordial nucleosynthesis",
    "heavy quark effective theory",
    "decay channels",
    "hadronic jets",
    "perturbation theory",
    "dark matter",
    "electromagnetic fields",
    "general relativity",
    "magnetohydrodynamics",
    "energy transfer",
    "atlas experiment",
    "large hadron collider",
    "neutrino experiments",
    "gravitational lensing",
    "bremsstrahlung",
    "effective field theory",
    "collider detectors",
    "hawking radiation",
    "symmetry breaking",
    "ckm matrix",
    "anomalous couplings",
    "extra dimensions",
    "photons",
    "air showers",
    "particle tracking",
    "particle identification",
    "fermions",
    "photon-photon scattering",
    "trigger systems",
    "sterile neutrinos",
    "branching fractions",
    "branching ratio",
    "renormalization group",
    "proton structure",
    "angular momentum conservation",
    "gluon jets",
    "scalar field theory",
    "composite higgs",
    "neutrino detectors",
    "supersymmetry",
    "heavy quarkonium",
    "leptogenesis",
    "inelastic scattering",
    "linear accelerator",
    "quantum field theory",
    "strong magnetic fields",
    "standard model",
    "event reconstruction",
    "domain walls",
    "jet physics",
    "quantum electrodynamics",
    "gauge theory",
    "neutrinos",
    "higgs boson decay",
    "squarks",
    "cosmic strings",
    "lattice qcd",
    "integrated luminosity",
    "supernova neutrinos",
    "parity violation",
    "cosmic rays",
    "water cherenkov detectors",
    "time projection chamber",
    "mesons",
    "particle interactions",
    "s-matrix",
    "strong interaction",
    "decay constants",
    "quantum gravity",
    "quantum decoherence",
    "spin alignment",
    "parton distribution functions",
    "accelerator physics",
    "synchrotron radiation",
    "weakly interacting massive particles",
    "asymptotic freedom",
    "neutrino mass",
    "charged leptons",
    "synchrotron light source",
    "high-energy physics",
    "black hole formation",
    "jet quenching",
    "cherenkov radiation",
    "neutral currents",
    "neutralinos",
    "feynman diagrams",
    "qcd phase transition",
    "superstring theory",
    "topological insulators"
}

from pathlib import Path
import pandas as pd
import time

main_dir = Path(r"D:\Новая папка (2)\all china\all china") #необходимо указать свой полный путь до папки
for sub_dir in main_dir.iterdir():
    for file_path in sub_dir.iterdir():
        with open(file_path, "r", encoding="utf-8") as f:
            print(file_path)
            table = pd.read_csv(file_path)
            try:
                for index, row in table.iterrows():
                    el = row["Index Keywords"]
                    try:
                        if el != None:
                            el = el.split("; ")
                            for elem in el:
                                elem = elem.strip().lower()
                                if elem.strip().lower() in high_energy_physics_keywords:
                                    row.append(row["Author full names", "Cited by", "Affiliations"])
                    except:
                        pass

            except:
                    for index, row in table.iterrows():
                        el = row["Ключевые слова указателя"]
                    try:
                        if el != None:
                            el = el.split("; ")
                            for elem in el:
                                elem = elem.strip().lower()
                                if elem in high_energy_physics_keywords:
                                    row.append(row["Author full names", "Цитирования", "Организации"])
                    except:
                        pass

start_time = 0
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
print(f"Время выполнения программы: {execution_time} секунд")


start_time = time.time()
rows = []
high_energy_physics_keywords = {
    "neutrino oscillations",
    "flavor physics",
    "deep inelastic scattering",
    "higgs boson",
    "beam energy",
    "hadronization",
    "cyclotron",
    "quark-gluon plasma",
    "beam dynamics",
    "higgs field",
    "energy frontier",
    "string theory",
    "perturbative qcd",
    "renormalization",
    "weak force",
    "quantum tunneling",
    "electromagnetic radiation",
    "magnetic monopoles",
    "gauge bosons",
    "atmospheric neutrinos",
    "bosons",
    "quantum chromodynamics",
    "majorana particles",
    "polarization",
    "neutrino telescopes",
    "calorimetry",
    "lattice gauge theory",
    "dark energy",
    "holographic principle",
    "primordial nucleosynthesis",
    "heavy quark effective theory",
    "decay channels",
    "hadronic jets",
    "perturbation theory",
    "dark matter",
    "electromagnetic fields",
    "general relativity",
    "magnetohydrodynamics",
    "energy transfer",
    "atlas experiment",
    "large hadron collider",
    "neutrino experiments",
    "gravitational lensing",
    "bremsstrahlung",
    "effective field theory",
    "collider detectors",
    "hawking radiation",
    "symmetry breaking",
    "ckm matrix",
    "anomalous couplings",
    "extra dimensions",
    "photons",
    "air showers",
    "particle tracking",
    "particle identification",
    "fermions",
    "photon-photon scattering",
    "trigger systems",
    "sterile neutrinos",
    "branching fractions",
    "branching ratio",
    "renormalization group",
    "proton structure",
    "angular momentum conservation",
    "gluon jets",
    "scalar field theory",
    "composite higgs",
    "neutrino detectors",
    "supersymmetry",
    "heavy quarkonium",
    "leptogenesis",
    "inelastic scattering",
    "linear accelerator",
    "quantum field theory",
    "strong magnetic fields",
    "standard model",
    "event reconstruction",
    "domain walls",
    "jet physics",
    "quantum electrodynamics",
    "gauge theory",
    "neutrinos",
    "higgs boson decay",
    "squarks",
    "cosmic strings",
    "lattice qcd",
    "integrated luminosity",
    "supernova neutrinos",
    "parity violation",
    "cosmic rays",
    "water cherenkov detectors",
    "time projection chamber",
    "mesons",
    "particle interactions",
    "s-matrix",
    "strong interaction",
    "decay constants",
    "quantum gravity",
    "quantum decoherence",
    "spin alignment",
    "parton distribution functions",
    "accelerator physics",
    "synchrotron radiation",
    "weakly interacting massive particles",
    "asymptotic freedom",
    "neutrino mass",
    "charged leptons",
    "synchrotron light source",
    "high-energy physics",
    "black hole formation",
    "jet quenching",
    "cherenkov radiation",
    "neutral currents",
    "neutralinos",
    "feynman diagrams",
    "qcd phase transition",
    "superstring theory",
    "topological insulators"
}
main_dir = Path(r"D:\Новая папка (2)\all china\all china") #необходимо указать свой полный путь до папки
for sub_dir in main_dir.iterdir():
    for file_path in sub_dir.iterdir():
        with open(file_path, "r", encoding="utf-8") as f:
            print(file_path)
            table = pd.read_csv(file_path)
            try:
                for index, row in table.iterrows():
                    el = row["Index Keywords"]
                try:
                    if el != None:
                        el = el.split("; ")
                        for elem in el:
                            elem = elem.strip().lower()
                            if elem.strip().lower() in high_energy_physics_keywords:
                                rows.append(row["Author full names"], row["Cited by"], row["Affiliations"])
                except:
                    pass
            except:
                for index, row in table.iterrows():
                    el = row["Ключевые слова указателя"]
                    try:
                        if el != None:
                            el = el.split("; ")
                            for elem in el:
                                elem = elem.strip().lower()
                                if elem in high_energy_physics_keywords:
                                    rows.append(row["Author full names"], row["Цитирования"], row["Организации"])
                    except:
                            pass
            
            
            end_time = time.time()  # время окончания выполнения
            execution_time = end_time - start_time  # вычисляем время выполнения
            print(len(rows))
            print(f"Время выполнения программы: {execution_time} секунд")
            from pathlib import Path
            import pandas as pd
            import time
            
            start_time = time.time()
            rows = []
            high_energy_physics_keywords = {
                "neutrino oscillations",
                "flavor physics",
                "deep inelastic scattering",
                "higgs boson",
                "beam energy",
                "hadronization",
                "cyclotron",
                "quark-gluon plasma",
                "beam dynamics",
                "higgs field",
                "energy frontier",
                "string theory",
                "perturbative qcd",
                "renormalization",
                "weak force",
                "quantum tunneling",
                "electromagnetic radiation",
                "magnetic monopoles",
                "gauge bosons",
                "atmospheric neutrinos",
                "bosons",
                "quantum chromodynamics",
                "majorana particles",
                "polarization",
                "neutrino telescopes",
                "calorimetry",
                "lattice gauge theory",
                "dark energy",
                "holographic principle",
                "primordial nucleosynthesis",
                "heavy quark effective theory",
                "decay channels",
                "hadronic jets",
                "perturbation theory",
                "dark matter",
                "electromagnetic fields",
                "general relativity",
                "magnetohydrodynamics",
                "energy transfer",
                "atlas experiment",
                "large hadron collider",
                "neutrino experiments",
                "gravitational lensing",
                "bremsstrahlung",
                "effective field theory",
                "collider detectors",
                "hawking radiation",
                "symmetry breaking",
                "ckm matrix",
                "anomalous couplings",
                "extra dimensions",
                "photons",
                "air showers",
                "particle tracking",
                "particle identification",
                "fermions",
                "photon-photon scattering",
                "trigger systems",
                "sterile neutrinos",
                "branching fractions",
                "branching ratio",
                "renormalization group",
                "proton structure",
                "angular momentum conservation",
                "gluon jets",
                "scalar field theory",
                "composite higgs",
                "neutrino detectors",
                "supersymmetry",
                "heavy quarkonium",
                "leptogenesis",
                "inelastic scattering",
                "linear accelerator",
                "quantum field theory",
                "strong magnetic fields",
                "standard model",
                "event reconstruction",
                "domain walls",
                "jet physics",
                "quantum electrodynamics",
                "gauge theory",
                "neutrinos",
                "higgs boson decay",
                "squarks",
                "cosmic strings",
                "lattice qcd",
                "integrated luminosity",
                "supernova neutrinos",
                "parity violation",
                "cosmic rays",
                "water cherenkov detectors",
                "time projection chamber",
                "mesons",
                "particle interactions",
                "s-matrix",
                "strong interaction",
                "decay constants",
                "quantum gravity",
                "quantum decoherence",
                "spin alignment",
                "parton distribution functions",
                "accelerator physics",
                "synchrotron radiation",
                "weakly interacting massive particles",
                "asymptotic freedom",
                "neutrino mass",
                "charged leptons",
                "synchrotron light source",
                "high-energy physics",
                "black hole formation",
                "jet quenching",
                "cherenkov radiation",
                "neutral currents",
                "neutralinos",
                "feynman diagrams",
                "qcd phase transition",
                "superstring theory",
                "topological insulators"
            }
            main_dir = Path(r"D:\Новая папка (2)\all china\all china") #необходимо указать свой полный путь до папки
            for sub_dir in main_dir.iterdir():
                for file_path in sub_dir.iterdir():
                    with open(file_path, "r", encoding="utf-8") as f:
                        print(file_path)
                        table = pd.read_csv(file_path)
                        try:
                            for index, row in table.iterrows():
                                el = row["Index Keywords"]
                                try:
                                    if el != None:
                                        el = el.split("; ")
                                        for elem in el:
                                            elem = elem.strip().lower()
                                            if elem.strip().lower() in high_energy_physics_keywords:
                                                a1 = row["Author full names"]
                                                a2 = row["Cited by"]
                                                a3 = row["Affiliations"]
                                                rows.append((a1, a2, a3))
                                except:
                                        pass
                        except:
                                for index, row in table.iterrows():
                                    el = row["Ключевые слова указателя"]
                                    try:
                                        if el != None:
                                            el = el.split("; ")
                                            for elem in el:
                                                elem = elem.strip().lower()
                                                if elem in high_energy_physics_keywords:
                                                    a1 = row["Author full names"]
                                                    a2 = row["Цитирования"]
                                                    a3 = row["Организации"]
                                                rows.append((a1, a2, a3))
                                    except:
                                            pass
                        
                        
                        end_time = time.time()  # время окончания выполнения
                        execution_time = end_time - start_time  # вычисляем время выполнения
                        print(len(rows))
                        print(f"Время выполнения программы: {execution_time} секунд")