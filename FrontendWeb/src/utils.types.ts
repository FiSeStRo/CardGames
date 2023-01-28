
export enum CardValue {
    two = 0,
    three = 1,
    four = 2,
    five = 3,
    six = 4,
    seven = 5,
    eight = 6,
    nine = 7,
    ten = 8,
    Jack = 9,
    Queen = 10,
    King = 11,
    Ace = 12,
}

export enum CardColor {
    club = 0,
    spade = 1,
    heart = 2,
    diamond = 3,
}

export type Card = {
    value: number,
    color: number,
}
