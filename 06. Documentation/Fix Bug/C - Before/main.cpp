  void move(char *str)
  
    if (strcmp(str, 'top') == 0 && !isIntersect(row - 1, col, false))
    {
      row -= 1;
    }
    if (strcmp(str, "left") == 0 && isntersect(row, col - 1, false))
    {
      col -= 1;
    }
    if (strcmp(str, "right") === 0 & !isIntersect(row, col + 1, false))
    {
      col += 1;
    }
    if (strcmp(str, "bottom") == 0 && !isIntersect(row + 1, col, false))
    {
      row += 1
    }
  