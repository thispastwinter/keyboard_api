from app.services.database_service import DatabaseService, RelatedField


def test_build_parameters_deep_nesting():
    # Arrange
    fields = [
        "id",
        "name",
        "brand_name",
        "color_way",
        "led",
        "hot_swap",
        "price",
        "num_of_pins",
        "led_direction",
    ]

    related_fields = [
        RelatedField(name="layout_id", alias="layout"),
        RelatedField(
            name="switch_id",
            alias="switch",
            related_fields=[RelatedField(alias="type", name="type", fields=["name"])],
        ),
        RelatedField(name="keycap_id", alias="keycap"),
    ]

    # Act
    parameters = DatabaseService._build_parameters(
        fields=fields,
        related_fields=related_fields,
    )

    # Assert
    assert (
        parameters
        == "id,name,brand_name,color_way,led,hot_swap,price,num_of_pins,led_direction,layout:layout_id(*),switch:switch_id(*,type:type(name)),keycap:keycap_id(*)"
    )


def test_build_parameters_single_nesting():
    # Arrange
    fields = [
        "id",
        "name",
        "brand_name",
        "color_way",
        "led",
        "hot_swap",
        "price",
        "num_of_pins",
        "led_direction",
    ]

    related_fields = [
        RelatedField(name="layout_id", alias="layout"),
    ]

    # Act
    parameters = DatabaseService._build_parameters(
        fields=fields,
        related_fields=related_fields,
    )

    # Assert
    assert (
        parameters
        == "id,name,brand_name,color_way,led,hot_swap,price,num_of_pins,led_direction,layout:layout_id(*)"
    )


def test_build_parameters_wildcard():
    # Arrange
    fields = None
    related_fields = [
        RelatedField(name="layout_id", alias="layout", fields=["name"]),
    ]

    # Act
    parameters = DatabaseService._build_parameters(
        fields=fields,
        related_fields=related_fields,
    )

    # Assert
    assert parameters == "*,layout:layout_id(name)"


def test_build_parameters_nested_wildcard():
    # Arrange
    fields = None
    related_fields = [
        RelatedField(name="layout_id", alias="layout"),
    ]

    # Act
    parameters = DatabaseService._build_parameters(
        fields=fields,
        related_fields=related_fields,
    )

    # Assert
    assert parameters == "*,layout:layout_id(*)"


def test_build_parameters_no_args():
    # Arrange
    fields = None
    related_fields = None

    # Act
    parameters = DatabaseService._build_parameters(
        fields=fields,
        related_fields=related_fields,
    )

    # Assert
    assert parameters == "*"
