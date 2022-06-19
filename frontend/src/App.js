import Header from "./components/Header";
import Offers from "./components/Offers";
import Statistics from "./components/Statistics";
import Districts from "./components/Districts";
import Streets from "./components/Streets";
import Container from "react-bootstrap/Container";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <Header />
      <Container>
        <Routes>
          <Route path="/oferty" element={<Offers />} />
          <Route path="/statystyki" element={<Statistics />} />
          <Route path="/dzielnica/:nazwa" element={<Districts />} />
          <Route path="/ulica/:nazwa" element={<Streets />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
