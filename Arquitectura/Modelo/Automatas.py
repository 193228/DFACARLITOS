from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
from visual_automata.fa.nfa import VisualNFA

def generarAutomataDeterminista(automata):
    automatadfa = DFA(
        states=automata["estados"],
        input_symbols=automata["lenguaje"],
        transitions=automata["transiciones"],
        initial_state=automata["estadoInicial"],
        final_states=automata["estadosFinales"]
    )
    return automatadfa

def generarAutomataNoDeterminista(automata):
    automatanfa = NFA(
        states=automata["estados"],
        input_symbols=automata["lenguaje"],
        transitions=automata["transiciones"],
        initial_state=automata["estadoInicial"],
        final_states=automata["estadosFinales"]
    )
    return automatanfa