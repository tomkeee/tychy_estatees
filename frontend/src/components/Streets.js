import { useState, useEffect } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useParams } from "react-router-dom";

const Streets = () => {
  const { nazwa } = useParams();
  console.log(nazwa);
  const [streets, setStreets] = useState([]);

  useEffect(() => {
    async function fetchStreets() {
      const { data } = await axios.get(
        `http://localhost:4444/tychy/streets?location=${nazwa}`
      );
      setStreets(data);
    }

    fetchStreets();
  }, []);

  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
  const ready_street_name = capitalizeFirstLetter(nazwa);

  return (
    <Row
      className="justify-content-md-center"
      style={{ marginTop: "5%", marginBottom: "5%" }}
    >
      <h2
        className={("display-5", "text-center")}
        style={{ marginBottom: "5%" }}
      >
        {ready_street_name}
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
            {streets.map((street) => (
              <tr>
                <td>{street.date}</td>
                <td>
                  {Math.round(street.flat_average_price)
                    .toString()
                    .replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}
                </td>
                <td>
                  {Math.round(street.flat_m2_average_price)
                    .toString()
                    .replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}
                </td>
                <td>{street.flat_number}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Col>
    </Row>
  );
};

export default Streets;
