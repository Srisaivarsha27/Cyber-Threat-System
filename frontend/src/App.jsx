import { useEffect, useState } from "react";
import { getThreats, getMalware, getVulnerabilities, getAttackers } from "./api";

function App() {
    const [threats, setThreats] = useState([]);
    const [malware, setMalware] = useState([]);
    const [vulnerabilities, setVulnerabilities] = useState([]);
    const [attackers, setAttackers] = useState([]);

    useEffect(() => {
        async function fetchData() {
            setThreats(await getThreats());
            setMalware(await getMalware());
            setVulnerabilities(await getVulnerabilities());
            setAttackers(await getAttackers());
        }
        fetchData();
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Cyber Security Dashboard</h1>

            <section className="mt-4">
                <h2 className="text-xl font-semibold">Threats</h2>
                <ul>
                    {threats.map((threat) => (
                        <li key={threat.id}>{threat.name} - {threat.category}</li>
                    ))}
                </ul>
            </section>

            <section className="mt-4">
                <h2 className="text-xl font-semibold">Malware</h2>
                <ul>
                    {malware.map((item) => (
                        <li key={item.id}>{item.name} - {item.category}</li>
                    ))}
                </ul>
            </section>

            <section className="mt-4">
                <h2 className="text-xl font-semibold">Vulnerabilities</h2>
                <ul>
                    {vulnerabilities.map((item) => (
                        <li key={item.id}>{item.name} - {item.category}</li>
                    ))}
                </ul>
            </section>

            <section className="mt-4">
                <h2 className="text-xl font-semibold">Attackers</h2>
                <ul>
                    {attackers.map((item) => (
                        <li key={item.id}>{item.name} - {item.category}</li>
                    ))}
                </ul>
            </section>
        </div>
    );
}

export default App;
