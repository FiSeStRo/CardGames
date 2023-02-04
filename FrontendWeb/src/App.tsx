import { Component, createSignal } from "solid-js";

import styles from "./App.module.css";
import { Card } from "./utils.types";
import { createCardDeck } from "./utils";
import { postHandResults } from "./apiCalls";

const App: Component = () => {
  const [deck, setDeck] = createSignal<Card[]>([]);

  return (
    <div class={styles.App}>
      <header class={styles.header}>
        <button
          onClick={() => {
            setDeck(() => createCardDeck());
          }}
        >
          {"create Deck"}
        </button>
        <button
          onClick={async () => {
            await postHandResults(deck());
          }}
        >
          {"Call Api"}
        </button>
      </header>
    </div>
  );
};

export default App;
