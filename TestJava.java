public class TestJava {
  static public class PhysicalAttack{


    int singleAttackDamage(){
      return 10;
    }
  
  
    int doubleAttackDamage(){
      int s = singleAttackDamage()  + singleAttackDamage();
      return s;
    }
  
  }
  
  
  static  public class FighterAttack extends PhysicalAttack{
  
    @Override
    int singleAttackDamage(){
      System.out.println("Called");
      return super.singleAttackDamage();
    }
  
    @Override
    int doubleAttackDamage(){
      return super.doubleAttackDamage();
    }
  }

  public static void main(String[] args) {
    FighterAttack fa = new FighterAttack();

    fa.doubleAttackDamage();
    
  }
  
}
