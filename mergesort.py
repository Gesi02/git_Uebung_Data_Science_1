<<<<<<< Updated upstream
def ASSIGNMENT(new_list, i, old_list, j):
=======
def assign_value(new_list, i, old_list, j):                                 # ASSIGNMENT() umbennnen: function names should be snake_case and all lowercase
    """Weist den Wert von alte_liste[j] der neue_liste[i] zu."""            # docstring hinzufügen, um Funktion zu erklären
>>>>>>> Stashed changes
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
figure, axis = plt.subplots(1,2, figsize=(12, 6))

# Ungeordnete Liste plotten
axis[0].bar(x, my_list, label='Ungeordnete Liste', color='lime')
axis[0].set_title('Liste vorm Sortieren')
axis[0].set_xlabel('Listeneintrag')
axis[0].set_ylabel('Wert')
axis[0].legend()

# Merge Sort auf die Liste anwenden
merge_sort(my_list)

# Geordnete Liste plotten
axis[1].bar(x, my_list, label='Geordnete Liste', color='magenta')
axis[1].set_title('Liste nach Sortieren mit Merge Sort')
axis[1].set_xlabel('Listeneintrag')
axis[1].set_ylabel('Wert')
axis[1].legend()

plt.tight_layout()
plt.show()