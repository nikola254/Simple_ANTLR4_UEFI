class ControlFlowAutomaton:
    # Состояния автомата
    STATE_START            = 0
    STATE_ENTER_MAIN       = 1
    STATE_ENTER_KEY        = 2
    STATE_EXIT_KEY         = 3
    STATE_ENTER_COND       = 4
    STATE_BRANCH_HOOK      = 5
    STATE_EXIT_HOOK        = 6
    STATE_BRANCH_RESET     = 7
    STATE_EXIT_RESET       = 8
    STATE_EXIT_COND        = 9
    STATE_EXIT_MAIN        = 10
    STATE_END              = 11
    STATE_ERROR            = -1

    # Определяем допустимые переходы в виде словаря: (текущее_состояние, событие) -> следующее_состояние
    transitions = {
        (STATE_START,           "ENTER_main"):        STATE_ENTER_MAIN,
        (STATE_ENTER_MAIN,      "ENTER_key"):         STATE_ENTER_KEY,
        (STATE_ENTER_KEY,       "EXIT_key"):          STATE_EXIT_KEY,
        (STATE_EXIT_KEY,        "ENTER_conditional"): STATE_ENTER_COND,
        # Альтернатива ветки hook
        (STATE_ENTER_COND,      "ENTER_hook"):        STATE_BRANCH_HOOK,
        (STATE_BRANCH_HOOK,     "EXIT_hook"):         STATE_EXIT_HOOK,
        (STATE_EXIT_HOOK,       "EXIT_conditional"):  STATE_EXIT_COND,
        # Альтернатива ветки reset
        (STATE_ENTER_COND,      "ENTER_reset"):       STATE_BRANCH_RESET,
        (STATE_BRANCH_RESET,    "EXIT_reset"):        STATE_EXIT_RESET,
        (STATE_EXIT_RESET,      "EXIT_conditional"):  STATE_EXIT_COND,
        (STATE_EXIT_COND,       "EXIT_main"):         STATE_EXIT_MAIN,
        (STATE_EXIT_MAIN,       ""):                  STATE_END  # Завершение
    }

    def __init__(self):
        self.state = self.STATE_START

    def process_event(self, event):
        key = (self.state, event)
        if key in self.transitions:
            self.state = self.transitions[key]
            return True
        else:
            self.state = self.STATE_ERROR
            return False

    def is_valid(self):
        return self.state == self.STATE_END

if __name__ == '__main__':
    # Пример корректного потока (с веткой hook)
    events_hook = [
        "ENTER_main",
        "ENTER_key",
        "EXIT_key",
        "ENTER_conditional",
        "ENTER_hook",
        "EXIT_hook",
        "EXIT_conditional",
        "EXIT_main"
    ]
    # Пример корректного потока (с веткой reset)
    events_reset = [
        "ENTER_main",
        "ENTER_key",
        "EXIT_key",
        "ENTER_conditional",
        "ENTER_reset",
        "EXIT_reset",
        "EXIT_conditional",
        "EXIT_main"
    ]

    # Выберем один из потоков для проверки
    events = events_hook  # или events_reset

    automaton = ControlFlowAutomaton()
    deviation = False
    for e in events:
        if not automaton.process_event(e):
            print(f"Deviation detected at event: {e}")
            deviation = True
            break

    if not deviation and automaton.is_valid():
        print("Control flow is valid.")
    else:
        print("Control flow deviation or incomplete.")
