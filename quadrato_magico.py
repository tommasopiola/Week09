import copy

class QuadratoMagico:
    def __init__(self):
        self._soluzioni = [] # Lista di soluzioni
        self._num_iterazioni = 0
        self._num_soluzioni = 0

    """
    def _genera_rimanenti(self, N):
        rimanenti = []
        for i in range(1, N*N+1):
            rimanenti.append(i)
    """

    def stampa_soluzione(self, soluzione, N):
        print("---------")
        for row in range(N):
            print( [ v for v in soluzione[row*N:(row+1)*N] ])
        print("---------")

    def risolvi_quadrato_magico(self, N):
        self._soluzioni = [] # Lista di soluzioni
        self._num_iterazioni = 0
        self._num_soluzioni = 0
        self._ricorsione([], set(range(1, N*N+1)), N) #self._genera_rimanenti()

    # Funzione utilizzata per verificare se la soluzione
    # CHE SI E' TROVATA sia valida o no
    def _is_soluzione_valida(self, parziale, N):

        # Numero magico
        M = (N*(N*N+1))/2

        # Verifica del vincolo sulle righe
        for row in range(N): # Per ognuna delle righe
            somma = 0
            sottolista = parziale[row*N:(row+1)*N] # Elementi di quella riga
            for elemento in sottolista:
                somma += elemento
            if somma != M:
                return False



        # Verifica del vincolo sulle colonne
        for col in range(N):
            somma = 0
            sottolista = parziale[0*N+col : (N-1)*N+col+1: N]
            for elemento in sottolista:
                somma += elemento
            if somma != M:
                return False

        # Verifica del vincolo sulla prima diagonale
        somma = 0
        for row_col in range(N):
            somma += parziale[row_col*N+row_col]
        if somma!=M:
            return False

        # Verifica del vincolo sulla seconda diagonale
        somma = 0
        for row_col in range(N):
            somma+= parziale[row_col*N+(N-1-row_col)]
        if somma!=M:
            return False

        # Tutti i vincoli soddisfatti
        return True


    # Funzione utilizzata per verificare se la soluzione
    # CHE SI STA TROVANDO (MENTRE LA SI TROVA) sia valida o no
    def _is_soluzione_valida_in_itinere(self, parziale, N):
        # Numero magico
        M = (N*(N*N+1))/2

        # Verifica del vincolo sulle righe
        n_righe = len(parziale)//N # Per le sole righe nella soluzione fino a quel momento
        for row in range(n_righe):
             somma = 0
             sottolista = parziale[row*N:(row+1)*N]
             for elemento in sottolista:
                 somma += elemento
             if somma != M:
                 return False

        # Verifica del vincolo sulle colonne
        n_col = max(len(parziale) - N*(N-1), 0) # Per le sole colonne nella soluzione fino a quel momento
        for col in range(n_col):
            somma = 0
            sottolista = parziale[0*N + col : (N-1)*N+col + 1: N]
            for elemento in sottolista:
                somma += elemento
            if somma != M:
                return False

        # Verifica del vincolo sulla prima diagonale
        if len(parziale) == N*N: # Effettuata solo se parziale ha lunghezza N*N
            somma = 0
            for riga_col in range(N):
                somma += parziale[riga_col*N + riga_col]
            if somma != M:
                return False


        # Verifica del vincolo sulla seconda diagonale
        if len(parziale) == N*(N-1)+1: # Effettuata solo se si è arrivati ad inserire in parziale il primo elemento dell'ultima riga
            somma = 0
            for riga_col in range(N):
                somma += parziale[riga_col * N + (N-1-riga_col)]
            if somma != M:
                return False

        # tutti vincoli soddisfatti
        return True





    def _ricorsione(self, parziale, rimanenti, N) :
        self._num_iterazioni+=1
        # Caso/condiz. terminale
        if len(parziale) == N*N:
            #print(parziale)
                                                       # Così si verifica la soluzione dopo averla trovata:
            if self._is_soluzione_valida(parziale, N): # lo si potrebbe anche fare mentre la si cerca, per risparmiare ancora
                self._num_soluzioni += 1
                self._soluzioni.append(copy.deepcopy(parziale))

        # Caso/condiz. ricorsiva
        else:
            # Per evitare di provare sempre tutti i numeri da 1 a N*N+1 si usa set di rimanenti
            for i in rimanenti: #range(1, N*N+1)
                """
                parziale.append(i)
                # Preparaz. della nuova lista di numeri rimanenti da provare
                nuovi_rimanenti = copy.deepcopy(rimanenti)
                nuovi_rimanenti.remove(i)
                self._ricorsione( parziale, nuovi_rimanenti, N )
                parziale.pop()
                """

                parziale.append(i)
                # In alternativa, o in aggiunta, si può verificare la soluzione mentre la si cerca
                if self._is_soluzione_valida_in_itinere(parziale, N):
                    # Preparaz. della nuova lista di numeri rimanenti da provare
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(i)
                    self._ricorsione( parziale, nuovi_rimanenti, N )
                parziale.pop()

if __name__ == '__main__':
    N = 3
    qm = QuadratoMagico()
    qm.risolvi_quadrato_magico(N)
    #print(qm._soluzioni)
    print(f"Risoluzione quadrato magico di lato N = {N} (numero magico M = {int((N*(N*N+1))/2)})")
    print(f"Numero iterazioni: {qm._num_iterazioni}")
    print(f"Numero soluzioni: {qm._num_soluzioni}")
    for soluzione in qm._soluzioni:
        qm.stampa_soluzione(soluzione, N)
