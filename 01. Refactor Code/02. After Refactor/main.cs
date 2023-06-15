public class Account {
  private int money;

  public Account(int money){
    this.money = money;

    public void wihtdraw(int amount){
      int temp = this.money - amount;
      return temp;
    }

    public int getMoney(){
      return (this.money <= 0) ? 0 : this.money;
    }

    public void setMoney(int newMoney){
      if(newMoney < 0){
        System.Diagnostics.Debug.WriteLine("Invalid Money!");
      }else{
        money = newMoney;
      }
    }
  }
}