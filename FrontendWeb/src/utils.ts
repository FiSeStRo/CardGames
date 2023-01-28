import { Card, CardColor } from "./utils.types";

export function createCardDeck():Array<Card>{
    let cardList: Card[] = [];
    for (let index = 0; index < 7; index++) {
        let cardColor = getRandomInt(3);
        let cardValue = getRandomInt(12);
        cardList.push({
            value: cardValue,
            color: cardColor,
        })
        
    }
    console.log(cardList)
    return cardList 
}

export function getRandomInt(max:number):number {
    return Math.floor(Math.random() * max);
  }