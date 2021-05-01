void main() {
  Map char = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
  };
  String vertMirror(str) {
    var listt = [];
    for (int i = str.length - 1; i > -1; i--) {
      listt.add(str[i]);
    }
    return (listt.join());
  }

  String hor_Mirror(str) {
    var listt = [];
    final o = str.length + 1;
    for (int i = 0; i < o; i++) {
      for (int x = 0; i < char.length; i++) {
        if (str[i] == char[x]) {
          if (x < 13) {
            listt.add(char[x + 13]);
          } else {
            if (x == 13) {
              listt.add(char[x]);
            } else {
              listt.add(char[x - 13]);
            }
          }
        }
      }
    }
    return (listt.join());
  }

  print(hor_Mirror('monaaaa'));
  print(vertMirror('Mona'));
}
