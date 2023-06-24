void move(char *str)
{
  if (strcmp(str, "top") == 0 && !isIntersect(row - 1, col, false))
  {
    row -= 1;
  }
  if (strcmp(str, "left") == 0 && !isIntersect(row, col - 1, false))
  {
    col -= 1;
  }
  if (strcmp(str, "right") == 0 && !isIntersect(row, col + 1, false))
  {
    col += 1;
  }
  if (strcmp(str, "bottom") == 0 && !isIntersect(row + 1, col, false))
  {
    row += 1;
  }
}

// Additional Notes from Chat GPT,
// Here are the changes I made:

// Changed the single quotes to double quotes in the strcmp calls. String literals should be enclosed in double quotes in C.
// Corrected a typo in the second if statement where isntersect should be isIntersect.
// Replaced === with == in the third if statement. C uses a double equals sign for equality comparison.
// Added a semicolon at the end of the row += 1; statement to fix the missing semicolon error.

// With these changes, the code should compile without errors.