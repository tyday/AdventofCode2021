'use strict';

// if (typeof String.prototype.trim === 'undefined') {
//   String.prototype.trim = function () {
//     return String(this).replace(/^\s+|\s+$/g, '');
//   };
// }

const timer = ms => new Promise(res => setTimeout(res, ms))

const COLOR = {
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
const DELAY = 200;

class Octopus {
  constructor(val,loc){
    this.val = val;
    this.loc = loc;
    this.neighbors = [];
    this.flashed = false;
  }
  get_text(){
    let text = COLOR.BLUE + this.val + COLOR.END
    if(this.val==0){
      text = COLOR.YELLOW + this.val + COLOR.END
    }
    return text
  }
}

class Grid {
  constructor(data){
    this.data = data
    this.grid = [...Array(data.length)].map(e=>Array(data.length))
    this.flashes = 0

    this.initialize_grid()

  }
  print_grid(){
    this.grid.forEach(row => {
      let out_text = ''
      row.forEach(squid => {
        out_text += squid.get_text()
      })
      console.log(out_text)
    });
  }

  initialize_grid(){
    for(let row = 0; row < this.data.length; row++){
      for(let col = 0; col < this.data[0].length; col++){
        this.grid[row][col] = new Octopus(this.data[row][col],this.data[row][col])
      }
    }
    for(let row = 0; row < this.data.length; row++){
      for(let col = 0; col < this.data[0].length; col++){
        let neighbors = []
        let min_row = (row>0) ? row - 1 : row
        let max_row = (row < this.data.length-1) ? row +2 : row + 1
        let min_col = (col>0) ? col - 1 : col
        let max_col = (col < this.data.length-1) ? col +2 : col + 1
        
        for(let neighbor_row = min_row; neighbor_row < max_row; neighbor_row++){
          for (let neighbor_col = min_col; neighbor_col <max_col;neighbor_col ++){
            if (neighbor_row != row && neighbor_col != col){
              neighbors.push(this.grid[neighbor_row][neighbor_col])
            }
          }
        }
        this.grid[row][col].neighbors = neighbors
      }
    }
  }

  initialize_html(){
    const anchor = document.getElementById("app")
    const grid_html = document.createElement("div");
    grid_html.classList.add("grid")

    let r = 0; // Row counter
    let c = 0; // column counter
    this.grid.forEach( row => {
      const row_html = document.createElement("div")
      row_html.classList.add("row")
      grid_html.appendChild(row_html)
      row.forEach( col => {
        const squid_html = document.createElement("div")
        squid_html.classList.add("squid")
        squid_html.setAttribute("id", `r${r}c${c}`)
        squid_html.innerHTML = col.val;
        row_html.appendChild(squid_html)
        r ++;
      })
      c ++;
      r = 0;

    })
    anchor.appendChild(grid_html)
  }


  energize_neighbors(neighbors){
    neighbors.forEach(neighbor => {
      neighbor.val += 1
    })
  }

  run_turn(){
    let energized = []
    let flashes = 0
    this.grid.forEach( row => {
      row.forEach( squid => {
        squid.val += 1
        squid.flashed = false
        if (squid.val > 9){
          flashes += 1
          squid.flashed = true
          squid.val = 0
          squid.neighbors.forEach(n => energized.push(n))

        }
      })
    })

    while(energized > 0){
      squid = energized.pop()
      if(squid.flashed == false){
        squid.val += 1
      }
      if(squid.val > 9){
        flashes ++;
        squid.flashed = true
        squid.val = 0
        squid.neighbors.forEach(n => energized.push(n))
      }
    }
    this.flashes += flashes
    if(flashes == this.grid.length * this.grid[0].length){
      return true
    }
    return false
  }
}



async function main() {
  let data = [];
  await fetch('test.txt')
    .then((response) => response.text())
    .then((d) => {
      data = d.split('\n');
    });
  
    let grid = new Grid(data)
    console.log("hello")
    grid.print_grid()
    grid.initialize_html()



  }
main()