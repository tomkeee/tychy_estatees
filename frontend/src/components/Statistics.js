import { useState, useEffect } from "react";
import axios from "axios";
import Table from 'react-bootstrap/Table';
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"



const Statistics = () => {

    const [stats, setStats] = useState([]);

    useEffect(() => {
        async function fetchStats() {
          const { data } = await axios.get(
            "http://localhost:4444/tychy/statistics/all",
          );
          setStats(data);
        }
        
        fetchStats();
    }, []);
    
    
    return (
        <Row className="justify-content-md-center" style={{"margin-top":"5%","margin-bottom":"5%" }}>
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
            {stats.map(stat => 
            (
                <tr>
                    <td>{stat.date}</td>
                    <td>{Math.round(stat.flat_average_price).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}</td>
                    <td>{Math.round(stat.flat_m2_average_price).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " zł"}</td>
                    <td>{stat.flat_number}</td>
                </tr>
                )
                )
            }
            </tbody>
            </Table>
            </Col>

        </Row>

    )
}

export default Statistics;