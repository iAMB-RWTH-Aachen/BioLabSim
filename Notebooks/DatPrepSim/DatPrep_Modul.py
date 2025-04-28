import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from random import uniform, randint, choice, seed
import matplotlib
DEBUG = False
if DEBUG:
    matplotlib.use("tkAgg")
print(matplotlib.get_backend())


class MonodModel:
    """
    The 'MonodModel' class stores all information about the bioprocess model and its properties.
    It now also includes options to introduce different types of random errors to simulate real-world experimental conditions.
    """

    def __init__(self, add_errors=False, apply_noise=False, apply_outliers=False, apply_missing_values=False):
        # Instance attributes
        self.__Organism = 'E. coli'
        self.__OperationMode = 'batch'
        self.__Params = {
            'u0': 0,  # Initial growth rate [h^-1]
            'umax': round(uniform(0.5, 1.1), 3),  # Maximal growth rate [h^-1] (default 0.5 - 1.1)
            'duration': 24,  # Process Duration [h]
            'Ks': round(uniform(7, 10), 3),  # Monod substrate affinity constant (default 7 - 10) [g/L]
            'Yx': round(uniform(0.4, 0.6), 3),  # Yield coefficient for growth on glucose (default 0.4 - 0.6) [g/g]
            'k1': round(uniform(0.05, 0.2), 3),  # Production rate of Product (default 0.05 - 0.2) [# h^-1]
        }
        self.__Conditions = {
            'S0': round(uniform(19, 21), 3),  # Initial substrate concentration [g/L]
            'P0': 0,  # Initial product concentration [g/L]
            'X0': round(uniform(0.05, 0.3), 3)  # Initial biomass concentration [g/L]
        }
        self.Results = {}
        self.add_errors = add_errors  # Flag to add errors
        # Error control flags
        self.apply_noise = apply_noise
        self.apply_outliers = apply_outliers
        self.apply_missing_values = apply_missing_values

    def calculate_monod(self):
        """
        Calculates Monod kinetics for current model instance and introduces errors if specified.
        """
        duration = self.__Params['duration']
        umax, Ks = self.__Params['umax'], self.__Params['Ks']
        Yx, k1 = self.__Params['Yx'], self.__Params['k1']
        S, P, X = [self.__Conditions['S0']], [self.__Conditions['P0']], [self.__Conditions['X0']]
        u = [self.__Params['u0']]

        for j in range(1, duration):
            new_u = umax * S[j - 1] / (Ks + S[j - 1])  # Change of µ
            u.append(max(new_u, 0))

            new_rX = u[j - 1] * X[j - 1]  # Derivative of Biomass
            X.append(X[j - 1] + new_rX)

            new_rS = -(new_rX / Yx)  # Derivative of substrate
            new_S = S[j - 1] + new_rS
            S.append(max(new_S, 0))

            new_rP = (k1 * u[j]) * X[j]  # Derivative of product
            P.append(P[j - 1] + new_rP)

        self.Results = {'X': X, 'S': S, 'P': P, 'u': u}

        # Introduce errors if required
        if self.add_errors:
            self.add_random_errors()

        return self.Results

    def add_random_errors(self, noise_level_X=0.05, noise_level_S=0.05, noise_level_P=0.1,
                          outliers_X=1, outliers_S=1, outliers_P=1,
                          missing_X=1, missing_S=1, missing_P=1):
        """
        Adds random errors (outliers, noise, missing values) to the generated Monod kinetics data based on specified flags.
        """
        X, S, P = self.Results['X'], self.Results['S'], self.Results['P']

        # Add random noise to Biomass, Substrate, and Product concentrations
        def add_noise(data, noise_level):
            noise = np.random.normal(0, noise_level * np.std(data), len(data))
            return [max(val + n, 0) for val, n in zip(data, noise)]

        # Add random outliers (less extreme)
        def add_outliers(data, n_outliers=1, multiplier_range=(2.5, 5.0)):
            for _ in range(n_outliers):
                idx = randint(0, len(data) - 1)
                multiplier = uniform(*multiplier_range)
                data[idx] *= multiplier * choice([-1, 1])
            return data

        # Add missing values
        def add_missing_values(data, n_missing=1):
            for _ in range(n_missing):
                idx = randint(0, len(data) - 1)
                data[idx] = np.nan
            return data

        # Apply errors based on specified flags
        if self.apply_noise:
            self.Results['X'] = add_noise(X, noise_level_X)
            self.Results['S'] = add_noise(S, noise_level_S)
            self.Results['P'] = add_noise(P, noise_level_P)

        if self.apply_outliers:
            self.Results['X'] = add_outliers(self.Results['X'], n_outliers=outliers_X)
            self.Results['S'] = add_outliers(self.Results['S'], n_outliers=outliers_S)
            self.Results['P'] = add_outliers(self.Results['P'], n_outliers=outliers_P)

        if self.apply_missing_values:
            self.Results['X'] = add_missing_values(self.Results['X'], n_missing=missing_X)
            self.Results['S'] = add_missing_values(self.Results['S'], n_missing=missing_S)
            self.Results['P'] = add_missing_values(self.Results['P'], n_missing=missing_P)

    def plot_results(self):
        """
        Returns plot of current model instance results (X, S, P vs. Time).
        Raises AttributeError if no results are stored inside the model when the method is called.
        """
        if not hasattr(self, 'Results'):
            raise AttributeError('No Results yet! Call MonodModel.calculate_monod() before plotting.')

        time = range(1, self.__Params['duration'] + 1)
        X, S, P = self.Results['X'], self.Results['S'], self.Results['P']

        plt.plot(time, X, 'r', label='Biomass [g/L]')
        plt.plot(time, S, 'g', label='Substrate [g/L]')
        plt.plot(time, P, 'b', label='Product [g/L]')
        plt.legend()
        plt.ylabel('Concentration [g/L]')
        plt.xlabel('Process Duration [h]')
        plt.title(f'Monod Model Simulation with{" no" if not self.add_errors else ""} Errors')
        plt.show()


import matplotlib.pyplot as plt
import numpy as np
import random


class Datensatz:
    """
    Die 'Datensatz' Klasse verwaltet mehrere Instanzen der MonodModel Klasse, um mehrere Datensätze zu generieren und zu verwalten.
    Jeder Datensatz kann unterschiedliche Kombinationen von Fehlern enthalten. Diese Klasse unterstützt die interne
    Festlegung von Fehlerverteilungen und bietet die Möglichkeit, vordefinierte Standarddatensätze zu generieren.
    """

    def __init__(self, n_datasets=10, random_seed=None, generate_custom_datasets=False, generate_defaults=True):
        """
        Initialisiert die Datensatz-Klasse.

        :param n_datasets: Anzahl der zu generierenden Datensätze (nur wenn generate_custom_datasets=True).
        :param random_seed: Zufallssamen für die Reproduzierbarkeit.
        :param generate_custom_datasets: Boolean, ob benutzerdefinierte Datensätze generiert werden sollen.
        :param generate_defaults: Boolean, ob Standard-Datensätze generiert werden sollen.
        """
        self.models = []  # Liste zur Speicherung der MonodModel-Instanzen
        self.results = []  # Liste zur Speicherung der Ergebnisse jeder Instanz
        self.n_datasets = n_datasets  # Anzahl der zu generierenden Datensätze
        self.random_seed = random_seed  # Zufallssamen für die Reproduzierbarkeit
        self.generate_custom_datasets = generate_custom_datasets  # Steuerung der Generierung von benutzerdefinierten Datensätzen
        self.generate_defaults = generate_defaults  # Steuerung der Generierung der Standard-Datensätze

        if self.random_seed is not None and type(self.random_seed) == int:
            seed(self.random_seed)  # Setzt den Zufallssamen für die Reproduzierbarkeit
            np.random.seed(self.random_seed)  # Setzt auch den Samen für numpy-Zufallsfunktionen
        else:
            raise ValueError("You need to set a random seed!")

        # Standard-Datensätze als separate Instanzen
        self.default_dataset_1 = None
        self.default_dataset_2 = None
        self.default_dataset_3 = None

        # Generiere benutzerdefinierte Datensätze nur, wenn es explizit angefordert wird
        if self.generate_custom_datasets:
            self.error_distribution = self._default_error_distribution()  # Interne Verteilung der Fehleroptionen
            self.error_options = self.calculate_error_options()  # Berechnet die Fehleroptionen auf Basis der Verteilung
            self.generate_datasets()  # Generiert benutzerdefinierte Datensätze bei der Initialisierung

        # Generiere Standard-Datensätze nur, wenn es explizit angefordert wird
        if self.generate_defaults:
            self.create_default_dataset_1()
            self.create_default_dataset_2()
            self.create_default_dataset_3()

    def _default_error_distribution(self):
        """
        Definiert die standardmäßige Fehlerverteilung.

        :return: Dictionary mit Fehleroptionen und ihrer prozentualen Verteilung.
        """
        return {
            'none': 50,
            'noise': 10,
            'outliers': 10,
            'missing': 10,
            'noise,outliers': 5,
            'noise,missing': 5,
            'outliers,missing': 5,
            'noise,outliers,missing': 5
        }

    def calculate_error_options(self):
        """
        Berechnet die Fehleroptionen basierend auf der angegebenen prozentualen Verteilung.

        :return: Liste der Fehleroptionen, die zur Erzeugung der Datensätze verwendet werden.
        """
        options = []
        total_percentage = sum(self.error_distribution.values())

        if total_percentage != 100:
            raise ValueError("Die Summe der prozentualen Verteilung muss 100 ergeben.")

        for error_option, percentage in self.error_distribution.items():
            count = int((percentage / 100) * self.n_datasets)
            # Split string to list if necessary (e.g., 'noise,outliers' -> ['noise', 'outliers'])
            error_list = error_option.split(',')
            options.extend([error_list] * count)

        # If there's any discrepancy due to rounding, adjust to match n_datasets
        while len(options) < self.n_datasets:
            options.append(['none'])  # Default to 'none' if needed

        # Shuffle options to randomize order
        np.random.shuffle(options)
        return options

    def generate_datasets(self):
        """
        Generiert mehrere benutzerdefinierte Datensätze mit verschiedenen Fehlerkonfigurationen basierend auf der Verteilung.
        """
        for errors in self.error_options:
            add_errors = 'none' not in errors
            apply_noise = 'noise' in errors
            apply_outliers = 'outliers' in errors
            apply_missing_values = 'missing' in errors

            model = MonodModel(
                add_errors=add_errors,
                apply_noise=apply_noise,
                apply_outliers=apply_outliers,
                apply_missing_values=apply_missing_values
            )
            result = model.calculate_monod()  # Berechnet Monod-Kinetik
            self.models.append(model)
            self.results.append(result)

    def create_default_dataset_1(self):
        """
        Erstellt eine separate Instanz von Datensatz für Standard-Datensatz 1.
        Vier MonodModelle, keine Fehler und jede Fehleroption einzeln.
        """
        if self.default_dataset_1 is None:
            # print("Erstelle Standard-Datensatz 1 (vier Modelle: keine Fehler und jede Fehleroption einzeln)")
            self.default_dataset_1 = Datensatz(
                n_datasets=4,
                random_seed=self.random_seed,
                generate_custom_datasets=True,
                generate_defaults=False
            )
            self.default_dataset_1.models = [
                MonodModel(add_errors=False),
                MonodModel(add_errors=True, apply_noise=True),
                MonodModel(add_errors=True, apply_outliers=True),
                MonodModel(add_errors=True, apply_missing_values=True)
            ]
            for model in self.default_dataset_1.models:
                model.calculate_monod()

    def create_default_dataset_2(self):
        """
        Erstellt eine separate Instanz von Datensatz für Standard-Datensatz 2.
        Kleiner Datensatz mit 10-20 Modellen und geringer Fehlerverteilung.
        """
        if self.default_dataset_2 is None:
            # print("Erstelle Standard-Datensatz 2 (kleiner Datensatz mit geringer Fehlerverteilung)")
            self.default_dataset_2 = Datensatz(
                n_datasets=20,  # Setze n_datasets auf 20 für den kleinen Datensatz
                random_seed=self.random_seed,
                generate_custom_datasets=False,
                generate_defaults=False
            )
            small_error_distribution = {
                'none': 60,
                'noise': 15,
                'outliers': 10,
                'missing': 15
            }
            self.default_dataset_2.error_distribution = small_error_distribution
            self.default_dataset_2.error_options = self.default_dataset_2.calculate_error_options()
            self.default_dataset_2.generate_datasets()

    def create_default_dataset_3(self):
        """
        Erstellt eine separate Instanz von Datensatz für Standard-Datensatz 3.
        Großer Datensatz mit über 1000 Modellen und voller Fehlerverteilung.
        """
        if self.default_dataset_3 is None:
            # print("Erstelle Standard-Datensatz 3 (großer Datensatz mit voller Fehlerverteilung)")
            self.default_dataset_3 = Datensatz(
                n_datasets=1000,  # Setze n_datasets auf 1000 für den großen Datensatz
                random_seed=self.random_seed,
                generate_custom_datasets=False,
                generate_defaults=False
            )
            large_error_distribution = {
                'none': 20,
                'noise': 15,
                'outliers': 15,
                'missing': 15,
                'noise,outliers': 10,
                'noise,missing': 10,
                'outliers,missing': 10,
                'noise,outliers,missing': 5
            }
            self.default_dataset_3.error_distribution = large_error_distribution
            self.default_dataset_3.error_options = self.default_dataset_3.calculate_error_options()
            self.default_dataset_3.generate_datasets()

    def plot_default_dataset_1(self):
        """
        Plottet Standard-Datensatz 1: Alle 4 Modelle in einer Grafik mit Subplots.
        """
        if not self.default_dataset_1:
            print("Standard-Datensatz 1 ist nicht generiert.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle("Standard-Datensatz 1: Verläufe von 4 Modellen")

        model_titles = ["Keine Fehler", "Rauschen", "Ausreißer", "Fehlende Werte"]
        for idx, (ax, model, title) in enumerate(zip(axes.flatten(), self.default_dataset_1.models, model_titles)):
            time = range(1, model.Results['X'].__len__() + 1)
            ax.plot(time, model.Results['X'], label='Biomasse [g/L]', color='r')
            ax.plot(time, model.Results['S'], label='Substrat [g/L]', color='g')
            ax.plot(time, model.Results['P'], label='Produkt [g/L]', color='b')
            ax.set_title(title)
            ax.set_xlabel('Zeit [h]')
            ax.set_ylabel('Konzentration [g/L]')
            ax.legend()

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def plot_default_dataset_2(self):
        """
        Plottet Standard-Datensatz 2: Mehrere Modelle in einer oder mehreren Graphiken mit Subplots.
        """
        if not self.default_dataset_2:
            print("Standard-Datensatz 2 ist nicht generiert.")
            return

        models_per_plot = 20  # Anzahl der Modelle pro Graphik
        total_models = len(self.default_dataset_2.models)

        for i in range(0, total_models, models_per_plot):
            fig, axes = plt.subplots(10, 2, figsize=(12, 30))
            fig.suptitle(
                f"Standard-Datensatz 2: Verläufe von Modellen {i + 1} bis {min(i + models_per_plot, total_models)}")

            for j, ax in enumerate(axes.flatten()):
                if i + j >= total_models:
                    break

                model = self.default_dataset_2.models[i + j]
                time = range(1, model.Results['X'].__len__() + 1)
                ax.plot(time, model.Results['X'], label='Biomasse [g/L]', color='r')
                ax.plot(time, model.Results['S'], label='Substrat [g/L]', color='g')
                ax.plot(time, model.Results['P'], label='Produkt [g/L]', color='b')
                ax.set_title(f"Modell {i + j + 1}")
                ax.set_xlabel('Zeit [h]')
                ax.set_ylabel('Konzentration [g/L]')
                ax.legend()

            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.show()

    def plot_default_dataset_3(self):
        """
        Plottet Standard-Datensatz 3: Zufällig 9 Modelle mit allen Fehlerarten in einer Graphik mit Subplots.
        """
        if not self.default_dataset_3:
            print("Standard-Datensatz 3 ist nicht generiert.")
            return

        # Stelle sicher, dass mindestens ein Modell pro Fehleroption dabei ist
        errors_options_present = set()

        for model in self.default_dataset_3.models:
            errors_present = []
            if model.apply_noise:
                errors_present.append('noise')
            if model.apply_outliers:
                errors_present.append('outliers')
            if model.apply_missing_values:
                errors_present.append('missing')
            if not errors_present:
                errors_present.append('none')
            errors_options_present.update(errors_present)

        # Wähle zufällig 9 Modelle aus, die alle Fehleroptionen abdecken
        selected_models = []
        remaining_models = self.default_dataset_3.models.copy()
        for error in errors_options_present:
            for model in remaining_models:
                if (model.apply_noise and error == 'noise') or \
                        (model.apply_outliers and error == 'outliers') or \
                        (model.apply_missing_values and error == 'missing') or \
                        (
                                not model.apply_noise and not model.apply_outliers and not model.apply_missing_values and error == 'none'):
                    selected_models.append(model)
                    remaining_models.remove(model)
                    break

        # Füge zufällige Modelle hinzu, bis wir 9 Modelle haben
        while len(selected_models) < 9:
            selected_models.append(random.choice(remaining_models))

        fig, axes = plt.subplots(3, 3, figsize=(15, 10))
        fig.suptitle("Standard-Datensatz 3: Zufällige 9 Modelle mit allen Fehlerarten")

        for idx, (ax, model) in enumerate(zip(axes.flatten(), selected_models)):
            time = range(1, model.Results['X'].__len__() + 1)
            ax.plot(time, model.Results['X'], label='Biomasse [g/L]', color='r')
            ax.plot(time, model.Results['S'], label='Substrat [g/L]', color='g')
            ax.plot(time, model.Results['P'], label='Produkt [g/L]', color='b')
            ax.set_title(f"Modell {idx + 1}")
            ax.set_xlabel('Zeit [h]')
            ax.set_ylabel('Konzentration [g/L]')
            ax.legend()

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def __getitem__(self, index):
        """
        Ermöglicht den listartigen Zugriff auf die generierten Datensätze.
        """
        if index < 0 or index >= len(self.models):
            raise IndexError("Index außerhalb des gültigen Bereichs")
        return self.models[index]

    def __len__(self):
        """
        Gibt die Anzahl der generierten MonodModel-Instanzen zurück.
        """
        return len(self.models)

    def plot_all_results(self):
        """
        Plottet die Ergebnisse aller generierten Datensätze.
        """
        for i, model in enumerate(self.models):
            print(f"Plotting Dataset {i + 1}")
            model.plot_results()
            # Entfernen Sie 'break', um alle Datensätze zu plotten
            break


if __name__ == '__main__':
    # Nur Standard-Datensätze generieren
    datensatz = Datensatz(
        random_seed=201623945,  # Zufallssamen für Reproduzierbarkeit
        generate_custom_datasets=False,  # Keine benutzerdefinierten Datensätze generieren
        generate_defaults=True  # Standard-Datensätze generieren
    )

    # Zugriff auf die Standard-Datensätze
    datensatz.plot_default_dataset_1()
    # datensatz.plot_default_dataset_2()
    # datensatz.plot_default_dataset_3()
