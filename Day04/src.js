'use strict';

if (typeof String.prototype.trim === 'undefined') {
  String.prototype.trim = function () {
    return String(this).replace(/^\s+|\s+$/g, '');
  };
}

let COLOR = {
  BLACK: '\x1b[30m',
  RED: '\x1b[31m',
  GREEN: '\x1b[32m',
  YELLOW: '\x1b[33m',
  BLUE: '\x1b[34m',
  MAGENTA: '\x1b[35m',
  CYAN: '\x1b[36m',
  GREY: '\x1b[37m',
  END: '\x1b[0m',
};

class Game {
  constructor() {
    this.turns = [];
    this.bingo_cards = {};
    this.positions = {};
  }

  simulate_game() {
    let games = [];
    for (const [key, value] of Object.entries(this.bingo_cards)) {
      games.push(value.id);
    }
    let turns = [...this.turns];
    let turn_count = 0;
    while (turns.length > 0) {
      let turn = turns.shift();
      this.positions[turn].forEach((position) => {
        let { card_id, row, col } = position.mark();
        let card = this.bingo_cards[card_id];
        let card_won = card.check_for_win(row, col, turn_count);
        if (card_won) {
          console.log(`Win on turn ${turn_count}`);
          console.log(`Last number called = ${turn}`);
          console.log(`Card ${card.id} won with ${card.value_at_win} points`);
          console.log(`Total: ${turn * card.value_at_win}`);
          if (games.indexOf(card_id) > -1) {
            let idx = games.indexOf(card_id);
            games.splice(idx, 1);
            if (games.length == 1) {
              console.log('Last Card');
            }
          }
        }
      });
      turn_count++;
    }
  }
}

class Position {
  constructor(val, col, row, card_number, marked) {
    this.val = val;
    this.col = col;
    this.row = row;
    this.card_number = card_number;
    this.marked = marked;
  }
  mark() {
    this.marked = true;
    return { card_id: this.card_number, row: this.row, col: this.col };
  }
  repr() {
    let value = `${this.val}`.padStart(2, '0');
    if (this.marked) return COLOR.RED + value + COLOR.END;
    else return value;
  }
  html() {
    let value = `${this.val}`.padStart(2, '0');
    if (this.marked) {
      value = `<span class='position marked'>${value}</>`;
    } else {
      value = `<span class='position'>${value}</>`;
    }
    return value;
  }
}

class Bingo_Card {
  constructor(matrix, id) {
    this.id = id;
    this.matrix = matrix;
    this.won = false;
    this.turn_won = null;
    this.value_at_win = 0;
  }
  display() {
    this.matrix.forEach((row) => {
      // console.log(row)
      let print_string = '';
      row.forEach((e) => (print_string += e.repr() + ' '));
      console.log(print_string);
    });
  }

  // is_row_complete(row) {
  //   let positions = this.matrix[row];
  //   positions.forEach((e) => {
  //     if (e.marked === false) {
  //       return false;
  //     }
  //   });
  //   return true;
  // }
  is_row_complete(row) {
    for (let col = 0; col < 5; col++) {
      if (this.matrix[row][col].marked === false) {
        return false;
      }
    }
    return true;
  }
  is_column_complete(column) {
    for (let row = 0; row < 5; row++) {
      if (this.matrix[row][column].marked === false) {
        return false;
      }
    }
    return true;
  }

  calculate_score() {
    let score = 0;
    this.matrix.forEach((row) => {
      row.forEach((position) => {
        if (position.marked === false) {
          score += position.val;
        }
      });
    });
    return score;
  }

  check_for_win(row, col, turn_count) {
    // If card has already won, just return false
    if (this.won) return false;

    if (this.is_row_complete(row)) {
      this.won = true;
      this.turn_won = turn_count;
      this.value_at_win = this.calculate_score();
      return true;
    } else if (this.is_column_complete(col)) {
      this.won = true;
      this.turn_won = turn_count;
      this.value_at_win = this.calculate_score();
      return true;
    } else {
      return false;
    }
  }
}

async function main() {
  let data = [];
  await fetch('day04.txt')
    .then((response) => response.text())
    .then((d) => {
      data = d.split('\n');
    });

  let game = new Game();
  let turns = data.shift();
  turns = turns.split(',').map((e) => Number(e));
  game.turns = turns;
  data.shift();

  let board_count = 0;
  // let matrix = Array(5).fill(Array(5).fill(null));
  let matrix = [
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
    [null, null, null, null, null],
  ];
  let row = 0;

  data.forEach((line) => {
    if (line == '') {
      // # We've reached the end of a bingo card
      //     # Add it to the Game object
      let card = new Bingo_Card(matrix, board_count);
      game.bingo_cards[board_count] = card;
      board_count += 1;
      // matrix = Array(5).fill(Array(5).fill(null));
      matrix = [
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null],
      ];
      row = 0;
    } else {
      let row_data = line
        .trim()
        .split(/[ ]+/)
        .map((e) => Number(e));

      for (let col = 0; col < 5; col++) {
        let val = row_data[col];
        let marked = false;
        let position = new Position(val, col, row, board_count, marked);
        matrix[row][col] = position;
        if (game.positions.hasOwnProperty(val)) {
          game.positions[val].push(position);
        } else {
          game.positions[val] = [position];
        }
      }
      row++;
    }
  });
  // console.log(game.positions);
  // game.bingo_cards[0].display();
  game.simulate_game();
}

main();
