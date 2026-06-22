<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LawAssistBot</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f4f6f9;
      color: #333;
      max-width: 900px;
      margin: auto;
      padding: 40px 20px;
    }

    h1 {
      text-align: center;
      color: #2c3e50;
      margin-bottom: 40px;
    }

    .section {
      background: white;
      padding: 25px 30px;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      margin-bottom: 30px;
    }

    .section h2 {
      color: #34495e;
      margin-bottom: 15px;
    }

    textarea, input, select, button {
      width: 100%;
      padding: 12px;
      margin-top: 10px;
      margin-bottom: 15px;
      font-size: 16px;
      border-radius: 6px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    button {
      background-color: #3498db;
      color: white;
      border: none;
      cursor: pointer;
      transition: background 0.3s ease;
    }

    button:hover {
      background-color: #2980b9;
    }

    .output {
      white-space: pre-wrap;
      background: #ecf0f1;
      border-left: 4px solid #2980b9;
      padding: 15px;
      border-radius: 6px;
      font-size: 15px;
    }

    footer {
      text-align: center;
      color: #aaa;
      margin-top: 40px;
      font-size: 14px;
    }
  </style>
</head>
<body>

  <h1>⚖️ LawAssistBot</h1>

  <div class="section">
    <h2>📄 Generate Legal Document</h2>
    <select id="docType">
      <option value="rental agreement">Rental Agreement</option>
      <option value="non-disclosure agreement">NDA</option>
    </select>
    <textarea id="docDetails" rows="5" placeholder='Enter details in JSON format...'></textarea>
    <button onclick="generateDocument()">Generate Document</button>
    <div class="output" id="docOutput"></div>
  </div>

  <div class="section">
    <h2>💡 Ask Legal Advice</h2>
    <textarea id="legalQuestion" rows="3" placeholder="Type your legal question here..."></textarea>
    <button onclick="askAdvice()">Get Advice</button>
    <div class="output" id="adviceOutput"></div>
  </div>

  <div class="section">
    <h2>🧾 Summarize Case</h2>
    <textarea id="caseText" rows="5" placeholder="Paste the case details to summarize..."></textarea>
    <button onclick="summarizeCase()">Summarize</button>
    <div class="output" id="summaryOutput"></div>
  </div>

<div class="section">
  <h2>📑 Analyze Legal PDF</h2>

  <input type="file" id="pdfFile" accept=".pdf">

  <button onclick="uploadPDF()">
    Analyze PDF
  </button>

<div id="riskBadge"></div>

  <div class="output" id="pdfOutput"></div>
  <button onclick="downloadReport()">
  📥 Download Report
</button>
</div>

<div class="section">

  <h2>📚 Legal Knowledge Search</h2>

  <textarea
    id="ragQuestion"
    rows="3"
    placeholder="Ask about laws, sections, articles...">
  </textarea>

  <button onclick="searchLaw()">
    Search
  </button>

  <div class="output" id="ragOutput"></div>

</div>

  <footer>
    &copy; 2025 LawAssistBot | Developed for LegalTech Innovations
  </footer>

  <script>
    const API_BASE = "http://127.0.0.1:8000";
    let latestAnalysis = "";

    async function generateDocument() {
      try {
        const type = document.getElementById("docType").value;
        const details = JSON.parse(document.getElementById("docDetails").value);
        const res = await fetch(`${API_BASE}/generate-document/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ type, details })
        });
        const data = await res.json();
        document.getElementById("docOutput").innerText = data.document || "❌ Error generating document.";
      } catch (err) {
        document.getElementById("docOutput").innerText = "⚠️ Invalid JSON format.";
      }
    }

    async function askAdvice() {
      const question = document.getElementById("legalQuestion").value;
      const res = await fetch(`${API_BASE}/legal-advice/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });
      const data = await res.json();
      document.getElementById("adviceOutput").innerText = data.advice || "❌ Error getting advice.";
    }

    async function summarizeCase() {
      const text = document.getElementById("caseText").value;
      const res = await fetch(`${API_BASE}/summarize/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      });
      const data = await res.json();
      document.getElementById("summaryOutput").innerText = data.summary || "❌ Error summarizing case.";
    }
    async function uploadPDF() {

  const fileInput = document.getElementById("pdfFile");

  if (!fileInput.files.length) {
    document.getElementById("pdfOutput").innerText =
      "⚠️ Please select a PDF file.";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  document.getElementById("pdfOutput").innerText =
    "⏳ Analyzing document...";

  try {

    const response = await fetch(
      `${API_BASE}/analyze-pdf`,
      {
        method: "POST",
        body: formData
      }
    );

    const data = await response.json();

    latestAnalysis = data.analysis;

    if (data.analysis.includes("High Risk")) {
      document.getElementById("riskBadge").innerHTML =
        "<h3 style='color:red'>🔴 HIGH RISK</h3>";
    } else if (data.analysis.includes("Medium Risk")) {
      document.getElementById("riskBadge").innerHTML =
        "<h3 style='color:orange'>🟠 MEDIUM RISK</h3>";
    } else if (data.analysis.includes("Low Risk")) {
      document.getElementById("riskBadge").innerHTML =
        "<h3 style='color:green'>🟢 LOW RISK</h3>";
    } else {
      document.getElementById("riskBadge").innerHTML = "";
    }

    document.getElementById("pdfOutput").innerText =
      data.analysis || "❌ Analysis failed.";
  } catch (error) {
    document.getElementById("pdfOutput").innerText =
      "❌ Error analyzing document.";
    console.error(error);
  }
}
async function downloadReport() {

  if (!latestAnalysis) {
    alert("No analysis available.");
    return;
  }

  const response = await fetch(
    `${API_BASE}/download-analysis`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        report: latestAnalysis
      })
    }
  );

  const blob = await response.blob();

  const url =
    window.URL.createObjectURL(blob);

  const a =
    document.createElement("a");

  a.href = url;
  a.download = "analysis_report.pdf";

  a.click();
}

async function searchLaw() {

  const question =
    document.getElementById("ragQuestion").value;

  const res =
    await fetch(
      `${API_BASE}/legal-search`,
      {
        method: "POST",
        headers: {
          "Content-Type":"application/json"
        },
        body: JSON.stringify({
          question
        })
      }
    );

  const data =
    await res.json();

  document.getElementById("ragOutput").innerText =
    data.answer;
}
  </script>

</body>
</html>
