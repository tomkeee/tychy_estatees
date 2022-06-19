import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import { districts, settlements } from "../utils/districts";
import { useState, useEffect } from "react";
import axios from "axios";

const Header = () => {
  const [streets, setStreets] = useState([]);

  useEffect(() => {
    async function fetchStreets() {
      const { data } = await axios.get(
        `http://localhost:4444/tychy/list/streets/`
      );
      setStreets(data);
    }

    fetchStreets();
  }, []);

  return (
    <Navbar bg="light" expanded="true">
      <Container>
        <Nav className="me-auto">
          <Nav.Link href="/oferty">Oferty</Nav.Link>
          <Nav.Link href="/statystyki">Statystyki</Nav.Link>

          <NavDropdown title="Dzielnice" id="basic-nav-dropdown">
            {districts.map((district) => (
              <NavDropdown.Item href={`/dzielnica/${district}`}>
                {district}
              </NavDropdown.Item>
            ))}
          </NavDropdown>

          <NavDropdown title="Osiedle" id="basic-nav-dropdown">
            {settlements.map((district) => (
              <NavDropdown.Item href={`/dzielnica/${district}`}>
                {district}
              </NavDropdown.Item>
            ))}
          </NavDropdown>

          <NavDropdown title="Ulice" id="basic-nav-dropdown">
            {streets.map((street) => (
              <NavDropdown.Item href={`/ulica/${street}`}>
                {street}
              </NavDropdown.Item>
            ))}
          </NavDropdown>
        </Nav>
      </Container>
    </Navbar>
  );
};
export default Header;
