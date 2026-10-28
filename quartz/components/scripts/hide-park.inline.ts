// Hide Park 사이트 스크립트: 헤딩 접기, 내부 링크 색(빈 페이지 구분)

const HEADING = /^H[1-6]$/

// 노트 템플릿의 뼈대 글자. 이것을 빼고 남는 글자가 없으면 빈 페이지로 본다.
const SCAFFOLD =
  /tl;dr|Info|Summary|Portfolio|People|Members|Key Concepts|Related Topics|Courses|Faculty|Discography|Studio Album|EP|Single|Track list|Content|\{\{title\}\}|\[\[\]\]/gi

let blankSlugs: Set<string> | undefined
const known = new Set<string>() // 노트가 있는 모든 slug

// 사이트 루트 경로 (예: /hide-park). 왼쪽 위 워드마크 링크로 알아낸다.
function siteRoot() {
  const home = document.querySelector<HTMLAnchorElement>(".page-title a")
  return decodeURIComponent(
    new URL(home?.getAttribute("href") ?? "/", window.location.href).pathname,
  ).replace(/\/+$/, "")
}

// 빈 페이지 = 본문에 뼈대 글자 말고는 없고, 속성(IG, Website 등)에도 값이 없는 노트
async function loadBlankSlugs() {
  if (blankSlugs) return blankSlugs
  blankSlugs = new Set()
  try {
    // @ts-ignore: renderPage 가 심어 두는 전역 (contentIndex.json 의 Promise)
    const index = await fetchData
    let withProps = new Set<string>()
    try {
      const res = await fetch(`${siteRoot()}/note-props.json`)
      if (res.ok) withProps = new Set<string>(await res.json())
    } catch {}
    for (const [slug, entry] of Object.entries<any>(index)) {
      known.add(slug)
      const text = String(entry.content ?? "")
        .replace(SCAFFOLD, " ")
        .replace(/[\s\W_]+/g, "")
      if (!text && !withProps.has(entry.filePath)) blankSlugs.add(slug)
    }
  } catch {}
  return blankSlugs
}

// 링크가 가리키는 페이지의 slug. 같은 페이지 안의 이동(#)이거나 사이트 밖이면 undefined
function targetSlug(a: HTMLAnchorElement, rootPath: string): string | undefined {
  const url = new URL(a.href, window.location.href)
  if (url.origin !== window.location.origin) return undefined
  if (url.pathname === window.location.pathname) return undefined
  let path = decodeURIComponent(url.pathname)
  if (!path.startsWith(rootPath)) return undefined
  path = path.slice(rootPath.length).replace(/^\/+/, "").replace(/\.html$/, "")
  if (path === "" || path.endsWith("/")) path += "index"
  return path
}

async function markLinks() {
  const links = document.querySelectorAll<HTMLAnchorElement>(
    "article a.internal:not([role='anchor']):not([data-footnote-ref]):not([data-footnote-backref])",
  )
  if (links.length === 0) return
  const blank = await loadBlankSlugs()
  const rootPath = siteRoot()
  for (const a of links) {
    const slug = targetSlug(a, rootPath)
    // 빈 페이지이거나, 링크만 있고 노트가 만들어지지 않은 경우(색인에 없음)
    const missing = slug !== undefined && known.size > 0 && !/\.[a-z0-9]{1,5}$/i.test(slug) && !known.has(slug)
    a.classList.toggle("hp-blank", slug !== undefined && (blank.has(slug) || missing))
  }
}

function headingLevel(el: Element) {
  return Number(el.tagName[1])
}

// 본문 바로 아래의 헤딩만 다룬다. 접힌 헤딩 아래(다음 같은/더 높은 헤딩 전까지)를 숨긴다.
function refreshFolds(container: Element) {
  let collapsedLevel: number | null = null
  for (const el of Array.from(container.children)) {
    if (HEADING.test(el.tagName)) {
      const level = headingLevel(el)
      if (collapsedLevel !== null && level <= collapsedLevel) collapsedLevel = null
      ;(el as HTMLElement).hidden = collapsedLevel !== null
      if (collapsedLevel === null && el.getAttribute("data-collapsed") === "true") {
        collapsedLevel = level
      }
    } else if (el.tagName !== "HR") {
      ;(el as HTMLElement).hidden = collapsedLevel !== null
    }
  }
}

function setupFolds() {
  const container = document.querySelector("article .markdown-rendered")
  if (!container) return
  const children = Array.from(container.children)
  children.forEach((el, i) => {
    if (!HEADING.test(el.tagName)) return
    const level = headingLevel(el)
    // 아래에 접을 내용이 있는 헤딩에만 토글을 단다
    let hasBody = false
    for (let j = i + 1; j < children.length; j++) {
      const next = children[j]
      if (HEADING.test(next.tagName) && headingLevel(next) <= level) break
      if (next.tagName !== "HR") {
        hasBody = true
        break
      }
    }
    if (!hasBody || el.querySelector(".hp-fold-toggle")) return
    const toggle = document.createElement("span")
    toggle.className = "hp-fold-toggle"
    toggle.setAttribute("role", "button")
    toggle.setAttribute("tabindex", "0")
    toggle.setAttribute("aria-label", "Toggle section")
    el.prepend(toggle)
    el.setAttribute("data-foldable", "true")
    el.setAttribute("data-collapsed", "false")
    toggle.setAttribute("aria-expanded", "true")
  })
}

function toggleHeading(heading: Element) {
  const collapsed = heading.getAttribute("data-collapsed") !== "true"
  heading.setAttribute("data-collapsed", String(collapsed))
  heading.querySelector(".hp-fold-toggle")?.setAttribute("aria-expanded", String(!collapsed))
  if (heading.parentElement) refreshFolds(heading.parentElement)
}

// 목차 등에서 접힌 구역 안의 헤딩으로 이동하면 펼친다
function revealHash() {
  const id = decodeURIComponent(window.location.hash.slice(1))
  const target = id ? document.getElementById(id) : null
  const container = target?.closest(".markdown-rendered")
  if (!target || !container) return
  let el: Element | null = target
  while (el && el.parentElement !== container) el = el.parentElement
  if (!el) return
  let changed = false
  const level = HEADING.test(el.tagName) ? headingLevel(el) : 7
  let min = level
  for (let p = el.previousElementSibling; p; p = p.previousElementSibling) {
    if (HEADING.test(p.tagName) && headingLevel(p) < min) {
      min = headingLevel(p)
      if (p.getAttribute("data-collapsed") === "true") {
        p.setAttribute("data-collapsed", "false")
        p.querySelector(".hp-fold-toggle")?.setAttribute("aria-expanded", "true")
        changed = true
      }
    }
  }
  if (changed) {
    refreshFolds(container)
    target.scrollIntoView()
  }
}

document.addEventListener("click", (e) => {
  const t = e.target as Element | null
  const heading = t?.closest(".markdown-rendered > h1, .markdown-rendered > h2, .markdown-rendered > h3, .markdown-rendered > h4, .markdown-rendered > h5, .markdown-rendered > h6")
  if (!heading || heading.getAttribute("data-foldable") !== "true") return
  if (t?.closest("a")) return
  toggleHeading(heading)
})

document.addEventListener("keydown", (e) => {
  if (e.key !== "Enter" && e.key !== " ") return
  const t = e.target as Element | null
  if (!t?.classList?.contains("hp-fold-toggle")) return
  e.preventDefault()
  const heading = t.parentElement
  if (heading) toggleHeading(heading)
})

document.addEventListener("nav", () => {
  setupFolds()
  markLinks()
  revealHash()
})

window.addEventListener("hashchange", revealHash)
