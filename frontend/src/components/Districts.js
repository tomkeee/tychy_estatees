import { useState, useEffect } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useParams } from "react-router-dom";

const Districts = () => {
  const { nazwa } = useParams();
  console.log(nazwa);
  const [districts, setDistricts] = useState([]);

  useEffect(() => {
    async function fetchDistricts() {
      const { data } = await axios.get(
        `http://localhost:4444/tychy/districts?location=${nazwa}`
      );
      setDistricts(data);
    }

    fetchDistricts();
  }, []);

  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
  const ready_district_name = capitalizeFirstLetter(nazwa);

  return (
    <Row
      className="justify-content-md-center"
      style={{ marginTop: "5%", marginBottom: "5%" }}
    >
      <h2
        className={("display-5", "text-center")}
        style={{ marginBottom: "5%" }}
      >
        {ready_district_name}
      </h2>
      <Col sm={12} md={12} lg={10} xl={10}>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Data</th>
              <th>Średnia cena za nieruchomości</th>
              <th>Średnia cena za m2</th>
              <th>liczba wystawionych nieruchomości</th>
            </tr>
          </thead>
          <tbody>
            {districts.map((district) => (
              <tr>
                <td>{district.date}</td>
                <td>
                  {Math.round(district.flat_average_price)
                    .toString()
                    .replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}
                </td>
                <td>
                  {Math.round(district.flat_m2_average_price)
                    .toString()
                    .replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}
                </td>
                <td>{district.flat_number}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Col>
    </Row>
  );
};

export default Districts;
