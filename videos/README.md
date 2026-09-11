# Hero media

## What the page uses now

- `../images/Congregation-v2.png` — the active first hero image. It is an AI-generated concept based on the real church-interior photograph and supplied parish-member reference photos, showing a multigenerational congregation exchanging the Sign of Peace, with adults in their 30s in front and adults in their 40s throughout the middle and rear.

The parish and recognizable people represented should approve its use and disclosure, or it should be replaced with an authentic parish photograph before launch.

## Older retained assets

- `hero-loop.mp4` — a placeholder. It is a slow pan built from the still photo `images/church-interior.jpg`. 1.5 MB, muted, no sound track. It loops.
- `hero-poster.jpg` — the first frame. The page shows it until the video can play, and always on slow connections, data saver, and for people who turn off motion.

Both are retained placeholders and are not currently shown on the homepage.

## How to restore a hero video later

`index.html` → section `.hero`:

```html
<video autoplay muted loop playsinline preload="metadata" poster="videos/hero-poster.jpg">
  <source src="videos/hero-loop.mp4" type="video/mp4">
</video>
```

`js/motion.js` does the rest:

- Does not autoplay if the visitor has `prefers-reduced-motion` on, or `saveData` on. The poster shows instead.
- Pauses the video when it scrolls off screen. Plays again when it comes back.
- A navy overlay sits on top (`--hero-overlay-a/b` in `css/tokens.css`), so the footage should be lighter and calmer than you think.

## What to shoot

One loop, 10 to 20 seconds. Quiet, wide, slow. No faces in close-up. No text in frame. Horizontal, 16:9.

Shot list, in order of preference:

1. The church exterior from the parking lot at golden hour, redwoods in frame, a few people walking in.
2. Inside the church before Mass. Light through the windows. People settling in, seen from behind.
3. Coffee and donuts in the hall after Mass. Hands, cups, conversation. Shot from the side, not from above.
4. Greeters at the door on a Welcome Weekend.
5. The Emerald Hills road up to the church, trees moving.

Avoid: fast pans, zooms, handheld shake, anything under 1 second per shot, anyone who has not given consent, children's faces.

## How to export

- Codec H.264, MP4 container. Add a WebM (VP9) version if you want a smaller file.
- 1920 × 1080. 24 or 30 fps.
- Target 2 to 4 MB total. Keep it under 5 MB.
- No audio track. Remove it; do not just mute it.
- Fade the last half second into the first half second so the loop does not jump.

Example with ffmpeg (installed on this Mac):

```bash
ffmpeg -i source.mov -t 15 -an -vf "scale=1920:-2,fps=30" -c:v libx264 -crf 26 -preset slow -movflags +faststart videos/hero-loop.mp4
```

Poster frame from the new video:

```bash
ffmpeg -i videos/hero-loop.mp4 -ss 0 -frames:v 1 -q:v 3 videos/hero-poster.jpg
```

## How to replace

1. Put the new files at `videos/hero-loop.mp4` and `videos/hero-poster.jpg`. Same names.
2. Open `http://localhost:8787` and reload. Nothing else changes.
3. Check the headline is still readable over the footage. If not, raise the overlay in `css/tokens.css` (`--hero-overlay-a`), not the footage.
