import numpy as np


def frobenius_norm(A):
    return np.linalg.norm(np.matrix(A),'fro')

def analyze(A):
    return(np.min(A), np.max(A), np.mean(A))

def infty_norm(A):
    return(np.linalg.norm(A,ord = np.inf))

# ==========================================================
# Bitte den Code ab hier nicht mehr verändern.
# Die unten stehenden Befehle testen Ihren Code automatisch!
#
# Es ist immer eine gute Idee, ein paar bekannte Testfälle
# für Ihre Funktionen zu implementieren! Dadurch können
# Fehler sehr früh im Entwicklungsprozess ausgeschlossen
# werden! Für mehr Informationen verweisen wir auf
# 
# ==========================================================
# a)
assert np.isclose(frobenius_norm(np.array([1])), 1)
assert np.isclose(frobenius_norm(np.ones((4,4))), 4)
assert np.isclose(frobenius_norm(np.array(
    [[1,2,1], [-1,2,-3], [0,1,-2]])), 5)
assert np.isclose(frobenius_norm(np.array([[1,2,3,4]])), np.sqrt(30))
print("Aufgabe a): OK")


# b)
assert np.all(np.isclose(analyze(np.array([1])), (1,1,1)))
assert np.all(np.isclose(analyze(np.array([-1, 1, 2])), (-1, 2, 2/3)))
assert np.all(np.isclose(analyze(np.diag([1,2,3,-5])), (-5, 3, 1/16)))
print("Aufgabe b): OK")

# c)
assert np.isclose(infty_norm(np.array([[-1,2,-3]])), 6)
assert np.isclose(infty_norm(np.eye(3)), 1)
assert np.isclose(infty_norm(np.array([[-1,2,1],[0,-2,3]])), 5)
print("Aufgabe c): OK")
