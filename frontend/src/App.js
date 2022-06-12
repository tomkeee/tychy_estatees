import Header from "./components/Header";
import Offers from "./components/Offers";
import Statistics from "./components/Statistics";
import Container from "react-bootstrap/Container"
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";


function App() {
  return (
    <Router>
      <Header />
      <Container>
        <Routes>

          <Route
            path="/oferty"
            element={
              <Offers />
            }
          />
           <Route
            path="/statystyki"
            element={
              <Statistics />
            }
          />
            
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
