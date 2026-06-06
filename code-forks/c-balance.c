/*
 * C (1972) — Imperative, explicit, dangerous ⚡
 * "The language that trusts you."
 *
 * Key constraints: manual memory, struct state, pointer mutation.
 * The balance is a struct field. Every function mutates it directly.
 * There is no borrow checker. There is no GC. There is only you and a segfault.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* — The State is a Struct — */
typedef struct {
    int balance;
    int target;
    int current_turn;
    int max_turns;
    int history[40];   /* fixed array — C doesn't grow */
    int history_len;
    char difficulty[8];
    int game_id;
} GameState;

/* — Functions mutate state directly via pointer — */
GameState* game_new(const char* difficulty) {
    GameState* g = malloc(sizeof(GameState));
    g->balance = 0;
    g->target = 0;
    g->current_turn = 0;
    g->max_turns = 20;
    g->history_len = 0;
    snprintf(g->difficulty, 8, "%s", difficulty);
    g->game_id = rand() % 1000;
    return g;
}

int apply_move(GameState* g, int delta) {
    if (delta < -1) delta = -1;
    if (delta > 1) delta = 1;

    /* Random perturbation */
    int perturbation = (rand() % 3) - 1;  /* -1, 0, or 1 */

    g->balance = g->balance + delta + perturbation;
    g->current_turn++;
    g->history[g->history_len++] = delta;

    return g->balance;
}

int decide_move(GameState* g) {
    /* C-style strategy: if-then-else, no frills */
    if (g->balance > 1) return -1;
    if (g->balance < -1) return 1;
    return 0;
}

void print_state(GameState* g) {
    printf("Game %d | Balance: %+d | Turn: %d/%d\n",
           g->game_id, g->balance, g->current_turn, g->max_turns);
}

int main() {
    srand(time(NULL));
    GameState* game = game_new("easy");

    /* Play 10 rounds (player + agent) */
    for (int i = 0; i < 10; i++) {
        int player_move = (rand() % 3) - 1;    /* random human */
        apply_move(game, player_move);

        int agent_move = decide_move(game);
        apply_move(game, agent_move);

        print_state(game);
    }

    free(game);  /* You must remember to free. C trusts you. */
    return 0;
}
