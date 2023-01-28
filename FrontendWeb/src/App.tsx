import { Component, createSignal } from "solid-js";

import styles from "./App.module.css";
import { Card } from "./utils.types";
import { createCardDeck } from "./utils";
import { getAssets } from "solid-js/web";
import { getCardResults } from "./apiCalls";

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
        {/* <For each={deck()}>{(item) => <div>{item.value}</div>}</For> */}
        <button
          onClick={async () => {
            await getCardResults(deck());
          }}
        >
          {" "}
          {"Call Api"}
        </button>
      </header>
    </div>
  );
};

export default App;
