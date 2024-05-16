import io.restassured.RestAssured;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class PetstoreAPITest {

    @BeforeClass
    public void setup() {
        RestAssured.baseURI = "https://petstore.swagger.io/v2";
    }

    @Test
    public void testGetPetById() {
        given()
            .pathParam("petId", 1)
        .when()
            .get("/pet/{petId}")
        .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("name", equalTo("Dog"));
    }

    @Test
    public void testGetInventory() {
        given()
        .when()
            .get("/store/inventory")
        .then()
            .statusCode(200);
    }
}
