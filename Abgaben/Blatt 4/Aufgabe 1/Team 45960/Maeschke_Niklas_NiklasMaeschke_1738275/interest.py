from math import log
def aktuelles_guthaben(anfangsbetrag,anzahl_tage,zinssatz):
    "berechnet aktuelles guthaben eines kontos abhängig von anfangsbetrag,anzahl_tage,zinssatz"
    return anfangsbetrag*((1+zinssatz/36000)**anzahl_tage)

def anfangsbetrag(aktuelles_guthaben,anzahl_tage,zinssatz):
    "berechnet anfangsbetrag auf einem konto abhängig von aktuelles_guthaben,anzahl_tage,zinssatz "
    return (aktuelles_guthaben/(1+zinssatz/36000)**anzahl_tage)

def anzahl_tage(anfangsbetrag,aktuelles_guthaben,zinssatz):
    "berechnet anzahl tage die geld auf einem konto ist mit anfangsbetrag,aktuelles_guthaben,zinssatz"
    return(log(aktuelles_guthaben/anfangsbetrag)/log(1+zinssatz/36000))

def zinssatz (anfangswert,aktuelles_guthaben,anzahl_tage):
    "berechnet zinssatz auf einem konto abhängig von anfangswert,aktuelles_guthaben,anzahl_tage)"
    zinssatz(36000*((aktuelles_guthaben/anfangsbetrag)**(1/anzahl_tage())-1))
