# 🔧 Code Forks — Language Paradigm Implementations

The same Ternary Balance game, implemented in languages spanning 1957–2024.
Each version reflects the language's unique philosophy, constraints, and worldview.

---

## Old Languages (1960–1999)

| # | Language | Year | Paradigm | File | Key Constraint |
|---|----------|------|----------|------|----------------|
| 1 | **C** | 1972 | Imperative, structured | `c-balance.c` | Manual memory, struct state |
| 2 | **LISP** | 1958 | Symbolic, recursion | `lisp-balance.lisp` | Everything is a list |
| 3 | **APL** | 1964 | Array-oriented | `apl-balance.apl` | Everything is an array |
| 4 | **Prolog** | 1972 | Logic programming | `prolog-balance.pl` | Declare truth, don't compute |
| 5 | **Haskell** | 1990 | Purely functional | `haskell-balance.hs` | No side effects, laziness |
| 6 | **SQL** | 1974 | Declarative, set-based | `sql-balance.sql` | State as relations |
| 7 | **Ada** | 1983 | Safety-critical | `ada-balance.adb` | Strong typing, contracts |
| 8 | **Perl** | 1987 | "There's more than one way" | `perl-balance.pl` | TMTOWTDI, regex, confusion |
| 9 | **OCaml** | 1996 | Industrial functional | `ocaml-balance.ml` | Type inference, algebraic types |
| 10 | **Python** | 1991 | "There should be one way" | `python-balance.py` | Executable pseudocode |

## Cutting-Edge Languages (2015–2024)

| # | Language | Year | Paradigm | File | Key Innovation |
|---|----------|------|----------|------|----------------|
| 11 | **Rust** | 2015 | Systems, ownership | `rust-balance.rs` | Borrow checker, no GC |
| 12 | **Go** | 2016 | Concurrent, simple | `go-balance.go` | Goroutines, channels |
| 13 | **Elixir** | 2016 | Actor, fault-tolerant | `elixir-balance.exs` | OTP, let-it-crash |
| 14 | **Zig** | 2016 | Comptime, no hidden allocs | `zig-balance.zig` | Compile-time execution |
| 15 | **Roc** | 2023 | Pattern-matching, no panics | `roc-balance.roc` | No runtime errors |
| 16 | **Bend** | 2024 | Automatic parallelism | `bend-balance.bend` | HVM2, implicit parallelism |
| 17 | **Mojo** | 2023 | Python + systems | `mojo-balance.mojo` | MLIR, `fn` and `def` |

---

## Comparative Analysis

### How "balance = 0" is expressed

| Language | Expression | Paradigm Meaning |
|----------|-----------|-----------------|
| C | `state.balance == 0` | Struct field comparison |
| LISP | `(eq (getf state ':balance) 0)` | Property on a plist |
| APL | `balance ≡ 0` | Array equality (scalar as 1×1) |
| Prolog | `balance(State, 0)` | Predicate is true |
| Haskell | `balance state == 0` | Pure function, no mutation |
| SQL | `SELECT balance FROM game WHERE balance = 0` | Set membership |
| Rust | `state.balance == 0` | Ownership-borrowed field |
| Go | `game.Balance == 0` | Goroutine-safe struct via channel |
| Elixir | `state.balance == 0` | Pattern-matched in GenServer |

### How "make a move" is expressed

| Language | Move Expression | Key Insight |
|----------|----------------|-------------|
| C | `state->balance += delta` | Direct mutation, pointer |
| LISP | `(setf (getf state ':balance) (+ (getf state ':balance) delta))` | Destructive update of plist |
| APL | `balance ← balance + delta` | Array addition |
| Prolog | `apply_move(State, Delta, NewState)` | New state derived from old |
| Haskell | `applyMove st d = st { balance = balance st + d }` | Purely functional update |
| SQL | `UPDATE game SET balance = balance + @delta` | Set-based mutation |
| Rust | `state.balance += delta` | Mutable borrow, safe |
| Go | `mu.Lock(); game.Balance += delta; mu.Unlock()` | Mutex-protected mutation |
| Elixir | `{:noreply, %{state | balance: state.balance + delta}}` | Immutable update in GenServer loop |

---

## The Insight

The same game looks completely different in each language — not because the *logic* changes, but because the *paradigm* changes how the programmer thinks about state, time, and transformation.

This mirrors the cultural forks:
- C = engineering room (precise, dangerous, powerful)
- Haskell = science room (pure, proven, accessible from both sides)
- Prolog = what would happen if the agent didn't act but simply *declared* what should be true
- Elixir = the agent and human as actors sending messages (정수 in code form)
- Bend = the agent doesn't choose one move — it tries ALL POSSIBLE MOVES in parallel
