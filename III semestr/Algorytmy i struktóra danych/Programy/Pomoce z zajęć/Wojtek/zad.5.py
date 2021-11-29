#(X+((Y*Z)/(W-V)))
#Bierze ( wrzuca na stos
#Bierze X wrzuca do wyniku
#+wrzuca na stos
#( wrzuca na stos
#( wrzuca na stos
#Y wrzuca do wrzucamy do wyrażenia
#*wrzucamy na stos
#Z wrzucamy do wyrażenia
#Gdy pojawia się nawias zamykający, wrzucamy pierwszy z  góry do wyrażenia
#W tym momencie wyrażenie wygląda: XYZ*
#Trafia na W, wrzuca do wyrażenia
#Trafia na -, wrzuca na stos
#V wrzuca do wyrażenia
#Napotyka ) zbiera - ze stosu i wrzuca do wyrażenia
#Znów ) zbiera ze stosu / i wrzuca do wyrażenia
#Trafia na ) i zbiera ze stosu + i dodaje do wyrażenia
#Końcowa wartość: XYZ*W V-/+