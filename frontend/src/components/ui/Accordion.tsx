import React, { useState } from 'react';
import { ChevronDown } from 'lucide-react';

export interface AccordionItem {
  id: string;
  title: string;
  content: React.ReactNode;
  subtitle?: string;
  badge?: string;
}

export interface AccordionProps {
  items: AccordionItem[];
  allowMultiple?: boolean;
  defaultExpandedIds?: string[];
}

export const Accordion: React.FC<AccordionProps> = ({
  items,
  allowMultiple = false,
  defaultExpandedIds = [],
}) => {
  const [expanded, setExpanded] = useState<Set<string>>(new Set(defaultExpandedIds));

  const toggleItem = (id: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        if (!allowMultiple) next.clear();
        next.add(id);
      }
      return next;
    });
  };

  return (
    <div className="accordion-root">
      {items.map((item) => {
        const isOpen = expanded.has(item.id);
        return (
          <div key={item.id} className={`accordion-card ${isOpen ? 'accordion-open' : ''}`}>
            <button
              type="button"
              className="accordion-header"
              onClick={() => toggleItem(item.id)}
              aria-expanded={isOpen}
            >
              <div className="accordion-title-block">
                <span className="accordion-title">{item.title}</span>
                {item.subtitle && <span className="accordion-subtitle">{item.subtitle}</span>}
              </div>
              <div className="accordion-meta-block">
                {item.badge && <span className="accordion-badge">{item.badge}</span>}
                <ChevronDown
                  size={18}
                  className={`accordion-chevron ${isOpen ? 'accordion-chevron-rotated' : ''}`}
                />
              </div>
            </button>
            {isOpen && <div className="accordion-content">{item.content}</div>}
          </div>
        );
      })}
    </div>
  );
};
