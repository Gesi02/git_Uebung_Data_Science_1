def assign_value(new_list, i, old_list, j):                                 # ASSIGNMENT() umbennnen: function names should be snake_case and all lowercase
    """Weist den Wert von alte_liste[j] der neue_liste[i] zu."""           # docstring hinzufügen, um Funktion zu erklären
    new_list[i] = old_list[j]


def merge_sort(list_to_sort):                                                               # mergeSort() umbennen: function names should be snake_case and all lowercase
    """Sortiert eine Liste in aufsteigender Reihenfolge mit dem Mergesort-Algorithmus."""   # docstring hinzufügen, um Funktion zu erklären
    if len(list_to_sort) > 1:                                                               # die beiden Bedingungen danach waren unnötig und wurden entfernt
        # Mitte der Liste finden
        mid = len(list_to_sort) // 2
        # Liste mithilfe der Mitte in zwei kleinere Listen aufteilen
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]

        # Rekursiv beide Listen sortieren
        merge_sort(left_half)
        merge_sort(right_half)

        # `l` und `r` sind die Zeiger für die linken und rechten Hälften, `i` ist der Zeiger für die Hauptliste.
        l = r = i = 0                                                                       # spart ein paar Zeilen

        # Die sortierten Hälften zusammenführen:

        # Elemente der beiden Hälften miteinander vergleichen, das kleinere Element in die Hauptliste kopieren.
        # Den entsprechende Zeiger (`l` oder `r`) erhöhen, sowie Zeiger `i`.
        while l < len(left_half) and r < len(right_half):
            if left_half[l] <= right_half[r]:
                assign_value(list_to_sort, i, left_half, l)                                # Funktionsaufruf vereinfachen: Simple is better than complex.

                l += 1
            else:
                assign_value(list_to_sort, i, right_half, r)                               # Funktionsaufruf vereinfachen: Simple is better than complex.
                r += 1
            i += 1

        # Verbleibende Elemente der linken Hälfte kopieren (falls nötig)
        while l < len(left_half):
            list_to_sort[i] = left_half[l]
            l += 1
            i += 1

        # Verbleibende Elemente der rechten Hälfte kopieren (falls nötig)
        while r < len(right_half):
            list_to_sort[i] = right_half[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
