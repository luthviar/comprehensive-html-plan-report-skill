#!/usr/bin/env python3
"""Validate the public generic HTML examples without third-party packages."""

from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILES = (ROOT / "PROJECT_PLAN_TEMPLATE.html", ROOT / "PROJECT_REPORT_TEMPLATE.html")
PRIVATE_PATTERNS = (
    re.compile(r"-----BEGIN [^-]+ PRIVATE KEY-----", re.IGNORECASE),
    re.compile(r"private_key\s*[:=]", re.IGNORECASE),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    re.compile(r"(?:^|[\"' =])/(?:Users|home)/"),
    re.compile(r"file:///", re.IGNORECASE),
    re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
)


class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.detail_groups = []
        self.detail_cards = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        ident = attrs.get("id")
        if ident:
            if ident in self.ids:
                raise AssertionError(f"duplicate id: {ident}")
            self.ids.add(ident)
        href = attrs.get("href", "")
        if href.startswith("#"):
            self.hrefs.append(href[1:])
        if tag == "details" and ident == "checklist-details":
            self.detail_groups.append(attrs)
        if tag == "article" and ident and ident.startswith("detail-"):
            self.detail_cards.append(ident)


def validate_html(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")
    lowered = raw.lower()
    for pattern in PRIVATE_PATTERNS:
        if pattern.search(raw):
            raise AssertionError(f"{path.name}: privacy pattern found: {pattern.pattern}")
    if "<script src=" in lowered or "<link href=\"http" in lowered or "src=\"http" in lowered:
        raise AssertionError(f"{path.name}: remote dependency found")

    audit = Audit()
    audit.feed(raw)
    if len(audit.detail_groups) != 1:
        raise AssertionError(f"{path.name}: expected one checklist detail toggle")
    if "open" in audit.detail_groups[0]:
        raise AssertionError(f"{path.name}: checklist details must be closed by default")
    if not audit.detail_cards:
        raise AssertionError(f"{path.name}: detail cards are missing")
    missing = sorted(set(audit.hrefs) - audit.ids)
    if missing:
        raise AssertionError(f"{path.name}: missing internal targets: {missing}")
    print(f"{path.name}: pass ({len(audit.detail_cards)} cards, {len(audit.hrefs)} internal links)")


for file in FILES:
    validate_html(file)
print("privacy and template validation: pass")
