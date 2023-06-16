public class Account
{
  private int money;
  public Account(int money)
  {
    this.money = money;
  }
  public int withdraw(int amount)
  {
    int temp = this.money - amount;
    return temp;
  }
}