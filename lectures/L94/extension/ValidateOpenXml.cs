using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Validation;
using System.Text.Json;
foreach(var file in args) {
using var doc = PresentationDocument.Open(file, false);
var validator = new OpenXmlValidator(FileFormatVersions.Office2019) { MaxNumberOfErrors = 0 };
var errors = validator.Validate(doc).Select(e => new {e.Id, Description=e.Description, Part=e.Part?.Uri.ToString(), Path=e.Path?.XPath}).ToList();
Console.WriteLine(JsonSerializer.Serialize(new {file, count=errors.Count, errors}, new JsonSerializerOptions {WriteIndented=true}));
}
