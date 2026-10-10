class Meal {

    private double cost;
    private boolean takeOut;
    private String main;
    private String drink;

    double getCost() {
        return this.cost;
    }

    boolean getTakeOut() {
        return this.takeOut;
    }

    String getMain() {
        return this.main;
    }

    String getDrink() {
        return this.drink;
    }

    void setCost(double cost) {
        this.cost = cost;
    }

    void setTakeOut(boolean takeOut) {
        this.takeOut = takeOut;
    }

    void setMain(String main) {
        this.main = main;
    }

    void setDrink(String drink) {
        this.drink = drink;
    }
}

class MealBuilder {

    private Meal myMeal;

    public MealBuilder() {
        myMeal = new Meal();
    }

    public MealBuilder addCost(double cost) {
        myMeal.setCost(cost);
        return this;
    }

    public MealBuilder addTakeOut(boolean takeOut) {
        myMeal.setTakeOut(takeOut);
        return this;
    }

    public MealBuilder addMainCourse(String main) {
        myMeal.setMain(main);
        return this;
    }

    public MealBuilder addDrink(String drink) {
        myMeal.setDrink(drink);
        return this;
    }

    Meal build() {
        return myMeal;
    }
}
